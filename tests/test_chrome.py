import asyncio
import copy
import json
import logging
import queue

import pytest
import websockets
from websockets.exceptions import ConnectionClosed


from chromewhip import chrome, helpers
from chromewhip.protocol import page

TEST_HOST = 'localhost'
TEST_PORT = 32322

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class ChromeMock:

    def __init__(self, host, port):
        self._tabs = []

    async def connect(self):
        tab = chrome.ChromeTab('test', 'about:blank', 'ws://%s:%s' % (TEST_HOST, TEST_PORT))
        self._tabs = [tab]

    @property
    def tabs(self):
        return self._tabs


@pytest.fixture
async def chrome_tab():
    """Ensure Chrome is running
    """
    browser = ChromeMock(host=TEST_HOST, port=TEST_PORT)
    await browser.connect()
    chrome_tab = browser.tabs[0]
    yield chrome_tab
    print("gracefully disconnecting chrome tab...")
    try:
        await chrome_tab.disconnect()
    except ConnectionClosed:
        pass

delay_s = int

def init_test_server(triggers: dict, initial_msgs: [dict] = None, expected: queue.Queue = None):
    async def test_server(websocket, path):
        """

        :param websocket:
        :param initial_msgs:
        :param triggers:
        :param expected: ordered sequence of messages expected to be sent by chromewhip
        :return:
        """
        log.info('Client connected! Starting handler!')
        if initial_msgs:
            for m in initial_msgs:
                await websocket.send(json.dumps(m, cls=helpers.ChromewhipJSONEncoder))

        c = 0

        while True:
            msg = await websocket.recv()
            log.info('Test server received message!')
            c += 1
            obj = json.loads(msg)

            if expected:
                try:
                    exp = expected.get(block=False)
                except queue.Empty:
                    pytest.fail('more messages received that expected')

                assert exp == obj, 'message number %s does not match, exp %s != recv %s' % (c, exp, obj)

            # either id or method
            is_method = False
            id_ = obj.get('id')

            if not id_:
                id_ = obj.get('method')
                if not id_:
                    pytest.fail('received invalid message, no id or method - %s ' % msg)
                is_method = True

            response_stream = triggers.get(id_)

            if not response_stream:
                pytest.fail('received unexpected message of %s = "%s"'
                            % ('method' if is_method else 'id', id_))

            if not len(response_stream):
                log.debug('expected message but no expected response, continue')

            log.debug('replying with payload "%s"' % response_stream)
            for r in response_stream:
                if isinstance(r, int):
                    await asyncio.sleep(r)
                else:
                    await websocket.send(json.dumps(r, cls=helpers.ChromewhipJSONEncoder))
    return test_server


@pytest.mark.asyncio
async def test_send_command_can_trigger_on_event_prior_to_commmand_containing_event_id(event_loop, chrome_tab):

    msg_id = 4
    frame_id = '3228.1'
    url = 'http://example.com'

    chrome_tab._message_id = msg_id - 1
    f = page.Frame(frame_id, 'test', url, 'test', 'text/html')
    p = page.Page.navigate(url)
    fe = page.FrameNavigatedEvent(f)

    ack = {'id': msg_id, 'result': {'frameId': frame_id}}
    triggers = {
        msg_id: [ack]
    }

    end_msg = copy.copy(p[0])
    end_msg['id'] = msg_id
    q = queue.Queue()
    q.put(end_msg)

    initial_msgs = [fe]

    test_server = init_test_server(triggers, initial_msgs=initial_msgs, expected=q)
    start_server = websockets.serve(test_server, TEST_HOST, TEST_PORT)
    server = await start_server
    await chrome_tab.connect()

    log.info('Sending command and awaiting...')
    result = await chrome_tab.send_command(p, await_on_event_type=page.FrameNavigatedEvent)
    assert result.get('ack') is not None
    assert result.get('event') is not None
    event = result.get('event')
    assert isinstance(event, page.FrameNavigatedEvent)
    assert event.frame.id == f.id
    assert event.frame.url == f.url

    server.close()
    await server.wait_closed()

@pytest.mark.asyncio
async def test_send_command_can_trigger_on_event_after_commmand_containing_event_id(event_loop, chrome_tab):
    msg_id = 4
    frame_id = '3228.1'
    url = 'http://example.com'

    chrome_tab._message_id = msg_id - 1
    f = page.Frame(frame_id, 'test', url, 'test', 'text/html')
    p = page.Page.navigate(url)
    fe = page.FrameNavigatedEvent(f)

    ack = {'id': msg_id, 'result': {'frameId': frame_id}}
    triggers = {
        msg_id: [ack, delay_s(1), fe]
    }

    end_msg = copy.copy(p[0])
    end_msg['id'] = msg_id
    q = queue.Queue()
    q.put(end_msg)

    test_server = init_test_server(triggers, expected=q)
    start_server = websockets.serve(test_server, TEST_HOST, TEST_PORT)
    server = await start_server
    await chrome_tab.connect()

    log.info('Sending command and awaiting...')
    result = await chrome_tab.send_command(p, await_on_event_type=page.FrameNavigatedEvent)
    assert result.get('ack') is not None
    assert result.get('event') is not None
    event = result.get('event')
    assert isinstance(event, page.FrameNavigatedEvent)
    assert event.frame.id == f.id
    assert event.frame.url == f.url

    server.close()
    await server.wait_closed()

@pytest.mark.asyncio
async def test_send_command_can_trigger_on_event_with_input_event(event_loop, chrome_tab):
    """test_send_command_can_trigger_on_event_with_input_event
    Below is test case that will workaround this issue
    https://github.com/chuckus/chromewhip/issues/2
    """
    msg_id = 4
    old_frame_id = '2000.1'
    frame_id = '3228.1'
    url = 'http://example.com'

    chrome_tab._message_id = msg_id - 1
    f = page.Frame(frame_id, 'test', url, 'test', 'text/html')
    p = page.Page.navigate(url)
    fe = page.FrameNavigatedEvent(f)
    fsle = page.FrameStoppedLoadingEvent(frame_id)

    # command ack is not related to proceeding events
    ack = {'id': msg_id, 'result': {'frameId': old_frame_id}}
    triggers = {
        msg_id: [ack, delay_s(1), fe, fsle]
    }

    end_msg = copy.copy(p[0])
    end_msg['id'] = msg_id
    q = queue.Queue()
    q.put(end_msg)

    test_server = init_test_server(triggers, expected=q)
    start_server = websockets.serve(test_server, TEST_HOST, TEST_PORT)
    server = await start_server
    await chrome_tab.connect()

    log.info('Sending command and awaiting...')
    result = await chrome_tab.send_command(p,
                                           input_event_type=page.FrameNavigatedEvent,
                                           await_on_event_type=page.FrameStoppedLoadingEvent)
    assert result.get('ack') is not None
    assert result.get('event') is not None
    event = result.get('event')
    assert isinstance(event, page.FrameStoppedLoadingEvent)
    assert event.frameId == f.id

    server.close()
    await server.wait_closed()
