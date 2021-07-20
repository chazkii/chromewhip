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
from chromewhip.protocol import network as Network

# LargestContentfulPaint: See https://github.com/WICG/LargestContentfulPaint and largest_contentful_paint.idl
class LargestContentfulPaint(ChromeTypeBase):
    def __init__(self,
                 renderTime: Union['Network.TimeSinceEpoch'],
                 loadTime: Union['Network.TimeSinceEpoch'],
                 size: Union['float'],
                 elementId: Optional['str'] = None,
                 url: Optional['str'] = None,
                 nodeId: Optional['DOM.BackendNodeId'] = None,
                 ):

        self.renderTime = renderTime
        self.loadTime = loadTime
        self.size = size
        self.elementId = elementId
        self.url = url
        self.nodeId = nodeId


# LayoutShiftAttribution: 
class LayoutShiftAttribution(ChromeTypeBase):
    def __init__(self,
                 previousRect: Union['DOM.Rect'],
                 currentRect: Union['DOM.Rect'],
                 nodeId: Optional['DOM.BackendNodeId'] = None,
                 ):

        self.previousRect = previousRect
        self.currentRect = currentRect
        self.nodeId = nodeId


# LayoutShift: See https://wicg.github.io/layout-instability/#sec-layout-shift and layout_shift.idl
class LayoutShift(ChromeTypeBase):
    def __init__(self,
                 value: Union['float'],
                 hadRecentInput: Union['bool'],
                 lastInputTime: Union['Network.TimeSinceEpoch'],
                 sources: Union['[LayoutShiftAttribution]'],
                 ):

        self.value = value
        self.hadRecentInput = hadRecentInput
        self.lastInputTime = lastInputTime
        self.sources = sources


# TimelineEvent: 
class TimelineEvent(ChromeTypeBase):
    def __init__(self,
                 frameId: Union['Page.FrameId'],
                 type: Union['str'],
                 name: Union['str'],
                 time: Union['Network.TimeSinceEpoch'],
                 duration: Optional['float'] = None,
                 lcpDetails: Optional['LargestContentfulPaint'] = None,
                 layoutShiftDetails: Optional['LayoutShift'] = None,
                 ):

        self.frameId = frameId
        self.type = type
        self.name = name
        self.time = time
        self.duration = duration
        self.lcpDetails = lcpDetails
        self.layoutShiftDetails = layoutShiftDetails


class PerformanceTimeline(PayloadMixin):
    """ Reporting of performance timeline events, as specified in
https://w3c.github.io/performance-timeline/#dom-performanceobserver.
    """
    @classmethod
    def enable(cls,
               eventTypes: Union['[]'],
               ):
        """Previously buffered events would be reported before method returns.
See also: timelineEventAdded
        :param eventTypes: The types of event to report, as specified in
https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype
The specified filter overrides any previous filters, passing empty
filter disables recording.
Note that not all types exposed to the web platform are currently supported.
        :type eventTypes: []
        """
        return (
            cls.build_send_payload("enable", {
                "eventTypes": eventTypes,
            }),
            None
        )



class TimelineEventAddedEvent(BaseEvent):

    js_name = 'Performancetimeline.timelineEventAdded'
    hashable = []
    is_hashable = False

    def __init__(self,
                 event: Union['TimelineEvent', dict],
                 ):
        if isinstance(event, dict):
            event = TimelineEvent(**event)
        self.event = event

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
