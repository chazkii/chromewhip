# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import dom as DOM
from chromewhip.protocol import debugger as Debugger
from chromewhip.protocol import runtime as Runtime

# DOMBreakpointType: DOM breakpoint type.
DOMBreakpointType = str

# CSPViolationType: CSP Violation type.
CSPViolationType = str

# EventListener: Object event listener.
class EventListener(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 useCapture: Union['bool'],
                 passive: Union['bool'],
                 once: Union['bool'],
                 scriptId: Union['Runtime.ScriptId'],
                 lineNumber: Union['int'],
                 columnNumber: Union['int'],
                 handler: Optional['Runtime.RemoteObject'] = None,
                 originalHandler: Optional['Runtime.RemoteObject'] = None,
                 backendNodeId: Optional['DOM.BackendNodeId'] = None,
                 ):

        self.type = type
        self.useCapture = useCapture
        self.passive = passive
        self.once = once
        self.scriptId = scriptId
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber
        self.handler = handler
        self.originalHandler = originalHandler
        self.backendNodeId = backendNodeId


class DOMDebugger(PayloadMixin):
    """ DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript
execution will stop on these operations as if there was a regular breakpoint set.
    """
    @classmethod
    def getEventListeners(cls,
                          objectId: Union['Runtime.RemoteObjectId'],
                          depth: Optional['int'] = None,
                          pierce: Optional['bool'] = None,
                          ):
        """Returns event listeners of the given object.
        :param objectId: Identifier of the object to return listeners for.
        :type objectId: Runtime.RemoteObjectId
        :param depth: The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
        :type depth: int
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false). Reports listeners for all contexts if pierce is enabled.
        :type pierce: bool
        """
        return (
            cls.build_send_payload("getEventListeners", {
                "objectId": objectId,
                "depth": depth,
                "pierce": pierce,
            }),
            cls.convert_payload({
                "listeners": {
                    "class": [EventListener],
                    "optional": False
                },
            })
        )

    @classmethod
    def removeDOMBreakpoint(cls,
                            nodeId: Union['DOM.NodeId'],
                            type: Union['DOMBreakpointType'],
                            ):
        """Removes DOM breakpoint that was set using `setDOMBreakpoint`.
        :param nodeId: Identifier of the node to remove breakpoint from.
        :type nodeId: DOM.NodeId
        :param type: Type of the breakpoint to remove.
        :type type: DOMBreakpointType
        """
        return (
            cls.build_send_payload("removeDOMBreakpoint", {
                "nodeId": nodeId,
                "type": type,
            }),
            None
        )

    @classmethod
    def removeEventListenerBreakpoint(cls,
                                      eventName: Union['str'],
                                      targetName: Optional['str'] = None,
                                      ):
        """Removes breakpoint on particular DOM event.
        :param eventName: Event name.
        :type eventName: str
        :param targetName: EventTarget interface name.
        :type targetName: str
        """
        return (
            cls.build_send_payload("removeEventListenerBreakpoint", {
                "eventName": eventName,
                "targetName": targetName,
            }),
            None
        )

    @classmethod
    def removeInstrumentationBreakpoint(cls,
                                        eventName: Union['str'],
                                        ):
        """Removes breakpoint on particular native event.
        :param eventName: Instrumentation name to stop on.
        :type eventName: str
        """
        return (
            cls.build_send_payload("removeInstrumentationBreakpoint", {
                "eventName": eventName,
            }),
            None
        )

    @classmethod
    def removeXHRBreakpoint(cls,
                            url: Union['str'],
                            ):
        """Removes breakpoint from XMLHttpRequest.
        :param url: Resource URL substring.
        :type url: str
        """
        return (
            cls.build_send_payload("removeXHRBreakpoint", {
                "url": url,
            }),
            None
        )

    @classmethod
    def setBreakOnCSPViolation(cls,
                               violationTypes: Union['[CSPViolationType]'],
                               ):
        """Sets breakpoint on particular CSP violations.
        :param violationTypes: CSP Violations to stop upon.
        :type violationTypes: [CSPViolationType]
        """
        return (
            cls.build_send_payload("setBreakOnCSPViolation", {
                "violationTypes": violationTypes,
            }),
            None
        )

    @classmethod
    def setDOMBreakpoint(cls,
                         nodeId: Union['DOM.NodeId'],
                         type: Union['DOMBreakpointType'],
                         ):
        """Sets breakpoint on particular operation with DOM.
        :param nodeId: Identifier of the node to set breakpoint on.
        :type nodeId: DOM.NodeId
        :param type: Type of the operation to stop upon.
        :type type: DOMBreakpointType
        """
        return (
            cls.build_send_payload("setDOMBreakpoint", {
                "nodeId": nodeId,
                "type": type,
            }),
            None
        )

    @classmethod
    def setEventListenerBreakpoint(cls,
                                   eventName: Union['str'],
                                   targetName: Optional['str'] = None,
                                   ):
        """Sets breakpoint on particular DOM event.
        :param eventName: DOM Event name to stop on (any DOM event will do).
        :type eventName: str
        :param targetName: EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any
EventTarget.
        :type targetName: str
        """
        return (
            cls.build_send_payload("setEventListenerBreakpoint", {
                "eventName": eventName,
                "targetName": targetName,
            }),
            None
        )

    @classmethod
    def setInstrumentationBreakpoint(cls,
                                     eventName: Union['str'],
                                     ):
        """Sets breakpoint on particular native event.
        :param eventName: Instrumentation name to stop on.
        :type eventName: str
        """
        return (
            cls.build_send_payload("setInstrumentationBreakpoint", {
                "eventName": eventName,
            }),
            None
        )

    @classmethod
    def setXHRBreakpoint(cls,
                         url: Union['str'],
                         ):
        """Sets breakpoint on XMLHttpRequest.
        :param url: Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        :type url: str
        """
        return (
            cls.build_send_payload("setXHRBreakpoint", {
                "url": url,
            }),
            None
        )

