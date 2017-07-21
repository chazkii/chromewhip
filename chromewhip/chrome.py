import asyncio
import base64
import json
import logging
from typing import Optional

import aiohttp
import websockets
import websockets.protocol

from chromewhip import helpers
from chromewhip.base import SyncAdder
from chromewhip.protocol import page, runtime, target, input, inspector, browser, accessibility

TIMEOUT_S = 30
MAX_PAYLOAD_SIZE_BYTES = 2 ** 23
MAX_PAYLOAD_SIZE_MB = MAX_PAYLOAD_SIZE_BYTES / 1024 ** 2


class ChromewhipException(Exception):
    pass


class TimeoutError(Exception):
    pass


class ProtocolError(ChromewhipException):
    pass


class JSScriptError(ChromewhipException):
    pass


class ChromeTab(metaclass=SyncAdder):

    def __init__(self, title, url, ws_uri):
        self._title = title
        self._url = url
        self._ws_uri = ws_uri
        self.target_id = ws_uri.split('/')[-1]
        self._ws: Optional[websockets.WebSocketClientProtocol] = None
        self._message_id = 0
        self._current_task: Optional[asyncio.Task] = None
        self._ack_events = {}
        self._ack_payloads = {}
        self._trigger_events = {}
        self._event_payloads = {}
        self._recv_task = None
        self._log = logging.getLogger('chromewhip.chrome.ChromeTab')
        self._send_log = logging.getLogger('chromewhip.chrome.ChromeTab.send_handler')
        self._recv_log = logging.getLogger('chromewhip.chrome.ChromeTab.recv_handler')

    async def connect(self):
        self._ws = await websockets.connect(self._ws_uri, max_size=MAX_PAYLOAD_SIZE_BYTES)  # 16MB
        self._recv_task = asyncio.ensure_future(self.recv_handler())
        self._log.info('Connected to Chrome tab %s' % self._ws_uri)

    async def disconnect(self):
        self._log.debug("Disconnecting tab...")
        if self._current_task and not self._current_task.done() and not self._current_task.cancelled():
            self._log.warning('Cancelling current task for websocket')
            self._current_task.cancel()
            await self._current_task
        if self._recv_task:
            self._recv_task.cancel()
            await self._recv_task

    async def recv_handler(self):
        try:
            while True:
                self._recv_log.debug('Waiting for message...')
                result = await self._ws.recv()
                self._recv_log.debug('Received message, processing...')

                if not result:
                    self._recv_log.error('Missing message, may have been a connection timeout...')
                    continue
                result = json.loads(result)

                if 'id' in result:
                    self._ack_payloads[result['id']] = result
                    ack_event = self._ack_events.get(result['id'])
                    if ack_event is None:
                        self._recv_log.error('Ignoring ack with id %s as no registered recv' % result['id'])
                        continue
                    self._recv_log.debug('Notifying ack event with id=%s' % (result['id']))
                    ack_event.set()

                elif 'method' in result:
                    self._recv_log.debug('Received event message!')
                    event = helpers.json_to_event(result)
                    hash_ = event.hash()
                    self._recv_log.debug('Received event with hash "%s", storing...' % hash)
                    # first, check if any requests are waiting upon it
                    self._event_payloads[hash_] = event
                    trigger_event = self._trigger_events.get(hash_)
                    if trigger_event:
                        self._recv_log.debug('trigger exists for hash "%s", alerting...' % hash_)
                        trigger_event.set()
                else:
                    self._recv_log.info('Invalid message %s, what do i do now?' % result)

        except asyncio.CancelledError:
            await self._ws.close()

    @staticmethod
    async def validator(result: dict, types: dict):
        for k, v in result.items():
            try:
                type_ = types[k]
            except KeyError:
                raise KeyError('%s not in expected payload of %s' % (k, types))
            if not isinstance(v, type_):
                raise ValueError('%s is not expected type %s, instead is %s' % (v, type_, type(v)))
        # await result
        return result

    async def _send(self, request, recv_validator=None, event_cls=None):
        self._message_id += 1
        request['id'] = self._message_id

        ack_event = asyncio.Event()
        self._ack_events[self._message_id] = ack_event

        if event_cls:
            if not event_cls.is_hashable:
                raise ValueError('Cannot trigger of event type "%s" as not hashable' % event_cls.__name__)

        result = {'ack': None, 'event': None}

        try:
            msg = json.dumps(request, cls=helpers.ChromewhipJSONEncoder)
            self._send_log.info('Sending command = %s' % msg)
            self._current_task = asyncio.ensure_future(self._ws.send(msg))
            await asyncio.wait_for(self._current_task, timeout=TIMEOUT_S)  # send

            self._send_log.debug('Waiting for ack event set for id=%s' % request['id'])
            await asyncio.wait_for(ack_event.wait(), timeout=TIMEOUT_S)  # recv
            self._send_log.debug('Received ack event set for id=%s' % request['id'])

            # ack_payload = self._ack_payloads[request['id']]
            ack_payload = self._ack_payloads.get(request['id'])
            if not ack_payload:
                self._send_log.error('Notified but no payload available for id=%s!' % request['id'])
                return result

            # check for errors
            error = ack_payload.get('error')

            if error:
                msg = '%s, code %s for id=%s' % (error.get('message', 'Unknown error'), error['code'], request['id'])
                self._send_log.error(msg)
                raise ProtocolError(msg)

            if recv_validator:
                self._send_log.debug('Validating recv payload for id=%s...' % request['id'])
                ack_result = recv_validator(ack_payload['result'])
                self._send_log.debug('Successful recv validation for id=%s...' % request['id'])
                ack_payload['result'] = ack_result

            result['ack'] = ack_payload

            if event_cls:
                # check if we've already received it
                # TODO: how to i match ack payload to event cls init params
                # - make a huge assumption that the ack payload are the hashable parts of event cls
                hash_ = event_cls.build_hash(**ack_result)
                event = self._event_payloads.get(hash_)
                if event:
                    self._send_log.debug('Fetching stored event with hash "%s"...' % hash_)
                    result['event'] = event
                else:
                    self._send_log.debug('Waiting for event with hash "%s"...' % hash_)
                    trigger_event = asyncio.Event()
                    self._trigger_events[hash_] = trigger_event
                    await asyncio.wait_for(trigger_event.wait(), timeout=TIMEOUT_S)  # recv
                    event = self._event_payloads.get(hash_)
                    if event:
                        result['event'] = event

            self._send_log.info('Successfully sent command = %s' % msg)
            return result
        except asyncio.TimeoutError:
            method = request['method']
            id_ = request['id']
            self._send_log.error(msg)
            if self._ws.state != websockets.protocol.OPEN:
                close_code = self._ws.close_code
                if close_code == 1002:
                    raise ProtocolError('Websocket protocol error occured for "%s" with id=%s' % (method, id_))
                elif close_code == 1006:
                    raise ProtocolError('Incomplete read error occured for "%s" with id=%s' % (method, id_))
                elif close_code == 1007:
                    raise ProtocolError('Unicode decode error occured for "%s" with id=%s' % (method, id_))
                elif close_code == 1009:
                    raise ProtocolError('Recv\'d payload exceeded %sMB for "%s" with id=%s, consider increasing this limit' % (MAX_PAYLOAD_SIZE_MB, method, id_))
            raise TimeoutError('Unknown cause for timeout to occurs for "%s" with id=%s' % (method, id_))

    async def new_message_handler(self, request):
        request['id'] = self._message_id
        await self._ws.send(json.dumps(request))
        return await self._ws.recv()

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def ws_uri(self):
        return self._ws_uri

    async def enable_page_events(self):
        return await self._send(*page.Page.enable())

    async def send_command(self, command, await_on_event_type=None):
        return await self._send(*command, event_cls=await_on_event_type)

    async def html(self):
        result = await self.evaluate('document.documentElement.outerHTML')
        value = result['ack']['result']['result'].value
        return value.encode('utf-8')

    async def screenshot(self):
        result = await self.send_command(page.Page.captureScreenshot(format='png', fromSurface=False))
        base64_data = result['ack']['result']['data']
        return base64.b64decode(base64_data)

    async def go(self, url):
        """
        Navigate the tab to the URL
        """
        # event = page.FrameNavigatedEvent
        event = page.FrameStoppedLoadingEvent
        return await self.send_command(page.Page.navigate(url), event)

    async def evaluate(self, javascript):
        """
        Evaluate JavaScript on the page
        """
        result = await self.send_command(runtime.Runtime.evaluate(javascript))
        r = result["ack"]["result"]["result"]
        if r.subtype == 'error':
            raise JSScriptError({
                'reason': 'Runtime.evalulate threw an error',
                'error': result["ack"]["result"]["exceptionDetails"].to_dict()
            })
        return result

    def __str__(self):
        return '%s - %s' % (self.title, self.url)

    def __repr__(self):
        return 'ChromeTab("%s", "%s", "%s")' % (self.title, self.url, self.ws_uri)


class Chrome(metaclass=SyncAdder):

    def __init__(self, host='localhost', port=9222):
        self._host = host
        self._port = port
        self._url = 'http://%s:%d' % (self.host, self.port)
        self._tabs = []
        self.is_connected = False
        self._log = logging.getLogger('chromewhip.chrome.Chrome')

    async def connect(self):
        """ Get all open browser tabs that are pages tabs
        """
        if not self.is_connected:
            try:
                await asyncio.wait_for(self.attempt_tab_fetch(), timeout=5)
            except TimeoutError:
                self._log.error('Unable to fetch tabs! Timeout')

    async def attempt_tab_fetch(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url + '/json') as resp:
                tabs = []
                data = await resp.json()
                if not len(data):
                    self._log.warning('Empty data, will attempt to reconnect until able to get pages.')
                for tab in filter(lambda x: x['type'] == 'page', data):
                    ws_url = tab.get('webSocketDebuggerUrl')
                    if not ws_url:
                        tab_id = tab['id']
                        ws_url = 'ws://{}:{}/devtools/page/{}'.format(self._host,
                                                                      self._port,
                                                                      tab_id)
                    t = ChromeTab(tab['title'], tab['url'], ws_url)
                    await t.connect()
                    tabs.append(t)
                self._tabs = tabs
                self._log.debug("Connected to Chrome! Found {} tabs".format(len(self._tabs)))
        self.is_connected = True


    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def url(self):
        return self._url

    @property
    def tabs(self):
        if not len(self._tabs):
            raise ValueError('Must call connect_s or connect first!')
        return tuple(self._tabs)

