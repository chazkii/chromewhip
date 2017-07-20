# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# TargetID: 
TargetID = str

# BrowserContextID: 
BrowserContextID = str

# TargetInfo: 
class TargetInfo(ChromeTypeBase):
    def __init__(self,
                 targetId: Union['TargetID'],
                 type: Union['str'],
                 title: Union['str'],
                 url: Union['str'],
                 attached: Union['bool'],
                 ):

        self.targetId = targetId
        self.type = type
        self.title = title
        self.url = url
        self.attached = attached


# RemoteLocation: 
class RemoteLocation(ChromeTypeBase):
    def __init__(self,
                 host: Union['str'],
                 port: Union['int'],
                 ):

        self.host = host
        self.port = port


class Target(PayloadMixin):
    """ Supports additional targets discovery and allows to attach to them.
    """
    @classmethod
    def setDiscoverTargets(cls,
                           discover: Union['bool'],
                           ):
        """Controls whether to discover available targets and notify via <code>targetCreated/targetInfoChanged/targetDestroyed</code> events.
        :param discover: Whether to discover available targets.
        :type discover: bool
        """
        return (
            cls.build_send_payload("setDiscoverTargets", {
                "discover": discover,
            }),
            None
        )

    @classmethod
    def setAutoAttach(cls,
                      autoAttach: Union['bool'],
                      waitForDebuggerOnStart: Union['bool'],
                      ):
        """Controls whether to automatically attach to new targets which are considered to be related to this one. When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all currently attached targets.
        :param autoAttach: Whether to auto-attach to related targets.
        :type autoAttach: bool
        :param waitForDebuggerOnStart: Whether to pause new targets when attaching to them. Use <code>Runtime.runIfWaitingForDebugger</code> to run paused targets.
        :type waitForDebuggerOnStart: bool
        """
        return (
            cls.build_send_payload("setAutoAttach", {
                "autoAttach": autoAttach,
                "waitForDebuggerOnStart": waitForDebuggerOnStart,
            }),
            None
        )

    @classmethod
    def setAttachToFrames(cls,
                          value: Union['bool'],
                          ):
        """
        :param value: Whether to attach to frames.
        :type value: bool
        """
        return (
            cls.build_send_payload("setAttachToFrames", {
                "value": value,
            }),
            None
        )

    @classmethod
    def setRemoteLocations(cls,
                           locations: Union['[RemoteLocation]'],
                           ):
        """Enables target discovery for the specified locations, when <code>setDiscoverTargets</code> was set to <code>true</code>.
        :param locations: List of remote locations.
        :type locations: [RemoteLocation]
        """
        return (
            cls.build_send_payload("setRemoteLocations", {
                "locations": locations,
            }),
            None
        )

    @classmethod
    def sendMessageToTarget(cls,
                            targetId: Union['TargetID'],
                            message: Union['str'],
                            ):
        """Sends protocol message to the target with given id.
        :param targetId: 
        :type targetId: TargetID
        :param message: 
        :type message: str
        """
        return (
            cls.build_send_payload("sendMessageToTarget", {
                "targetId": targetId,
                "message": message,
            }),
            None
        )

    @classmethod
    def getTargetInfo(cls,
                      targetId: Union['TargetID'],
                      ):
        """Returns information about a target.
        :param targetId: 
        :type targetId: TargetID
        """
        return (
            cls.build_send_payload("getTargetInfo", {
                "targetId": targetId,
            }),
            cls.convert_payload({
                "targetInfo": {
                    "class": TargetInfo,
                    "optional": False
                },
            })
        )

    @classmethod
    def activateTarget(cls,
                       targetId: Union['TargetID'],
                       ):
        """Activates (focuses) the target.
        :param targetId: 
        :type targetId: TargetID
        """
        return (
            cls.build_send_payload("activateTarget", {
                "targetId": targetId,
            }),
            None
        )

    @classmethod
    def closeTarget(cls,
                    targetId: Union['TargetID'],
                    ):
        """Closes the target. If the target is a page that gets closed too.
        :param targetId: 
        :type targetId: TargetID
        """
        return (
            cls.build_send_payload("closeTarget", {
                "targetId": targetId,
            }),
            cls.convert_payload({
                "success": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def attachToTarget(cls,
                       targetId: Union['TargetID'],
                       ):
        """Attaches to the target with given id.
        :param targetId: 
        :type targetId: TargetID
        """
        return (
            cls.build_send_payload("attachToTarget", {
                "targetId": targetId,
            }),
            cls.convert_payload({
                "success": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def detachFromTarget(cls,
                         targetId: Union['TargetID'],
                         ):
        """Detaches from the target with given id.
        :param targetId: 
        :type targetId: TargetID
        """
        return (
            cls.build_send_payload("detachFromTarget", {
                "targetId": targetId,
            }),
            None
        )

    @classmethod
    def createBrowserContext(cls):
        """Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than one.
        """
        return (
            cls.build_send_payload("createBrowserContext", {
            }),
            cls.convert_payload({
                "browserContextId": {
                    "class": BrowserContextID,
                    "optional": False
                },
            })
        )

    @classmethod
    def disposeBrowserContext(cls,
                              browserContextId: Union['BrowserContextID'],
                              ):
        """Deletes a BrowserContext, will fail of any open page uses it.
        :param browserContextId: 
        :type browserContextId: BrowserContextID
        """
        return (
            cls.build_send_payload("disposeBrowserContext", {
                "browserContextId": browserContextId,
            }),
            cls.convert_payload({
                "success": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def createTarget(cls,
                     url: Union['str'],
                     width: Optional['int'] = None,
                     height: Optional['int'] = None,
                     browserContextId: Optional['BrowserContextID'] = None,
                     ):
        """Creates a new page.
        :param url: The initial URL the page will be navigated to.
        :type url: str
        :param width: Frame width in DIP (headless chrome only).
        :type width: int
        :param height: Frame height in DIP (headless chrome only).
        :type height: int
        :param browserContextId: The browser context to create the page in (headless chrome only).
        :type browserContextId: BrowserContextID
        """
        return (
            cls.build_send_payload("createTarget", {
                "url": url,
                "width": width,
                "height": height,
                "browserContextId": browserContextId,
            }),
            cls.convert_payload({
                "targetId": {
                    "class": TargetID,
                    "optional": False
                },
            })
        )

    @classmethod
    def getTargets(cls):
        """Retrieves a list of available targets.
        """
        return (
            cls.build_send_payload("getTargets", {
            }),
            cls.convert_payload({
                "targetInfos": {
                    "class": [TargetInfo],
                    "optional": False
                },
            })
        )



class TargetCreatedEvent(BaseEvent):

    js_name = 'Target.targetCreated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 targetInfo: Union['TargetInfo', dict],
                 ):
        if isinstance(targetInfo, dict):
            targetInfo = TargetInfo(**targetInfo)
        self.targetInfo = targetInfo

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class TargetInfoChangedEvent(BaseEvent):

    js_name = 'Target.targetInfoChanged'
    hashable = []
    is_hashable = False

    def __init__(self,
                 targetInfo: Union['TargetInfo', dict],
                 ):
        if isinstance(targetInfo, dict):
            targetInfo = TargetInfo(**targetInfo)
        self.targetInfo = targetInfo

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class TargetDestroyedEvent(BaseEvent):

    js_name = 'Target.targetDestroyed'
    hashable = ['targetId']
    is_hashable = True

    def __init__(self,
                 targetId: Union['TargetID', dict],
                 ):
        if isinstance(targetId, dict):
            targetId = TargetID(**targetId)
        self.targetId = targetId

    @classmethod
    def build_hash(cls, targetId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class AttachedToTargetEvent(BaseEvent):

    js_name = 'Target.attachedToTarget'
    hashable = []
    is_hashable = False

    def __init__(self,
                 targetInfo: Union['TargetInfo', dict],
                 waitingForDebugger: Union['bool', dict],
                 ):
        if isinstance(targetInfo, dict):
            targetInfo = TargetInfo(**targetInfo)
        self.targetInfo = targetInfo
        if isinstance(waitingForDebugger, dict):
            waitingForDebugger = bool(**waitingForDebugger)
        self.waitingForDebugger = waitingForDebugger

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class DetachedFromTargetEvent(BaseEvent):

    js_name = 'Target.detachedFromTarget'
    hashable = ['targetId']
    is_hashable = True

    def __init__(self,
                 targetId: Union['TargetID', dict],
                 ):
        if isinstance(targetId, dict):
            targetId = TargetID(**targetId)
        self.targetId = targetId

    @classmethod
    def build_hash(cls, targetId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ReceivedMessageFromTargetEvent(BaseEvent):

    js_name = 'Target.receivedMessageFromTarget'
    hashable = ['targetId']
    is_hashable = True

    def __init__(self,
                 targetId: Union['TargetID', dict],
                 message: Union['str', dict],
                 ):
        if isinstance(targetId, dict):
            targetId = TargetID(**targetId)
        self.targetId = targetId
        if isinstance(message, dict):
            message = str(**message)
        self.message = message

    @classmethod
    def build_hash(cls, targetId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
