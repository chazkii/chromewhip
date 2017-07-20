# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import dom as DOM

# ScreenOrientation: Screen orientation.
class ScreenOrientation(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 angle: Union['int'],
                 ):

        self.type = type
        self.angle = angle


# VirtualTimePolicy: advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to allow the next delayed task (if any) to run; pause: The virtual time base may not advance; pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending resource fetches.
VirtualTimePolicy = str

class Emulation(PayloadMixin):
    """ This domain emulates different environments for the page.
    """
    @classmethod
    def setDeviceMetricsOverride(cls,
                                 width: Union['int'],
                                 height: Union['int'],
                                 deviceScaleFactor: Union['float'],
                                 mobile: Union['bool'],
                                 fitWindow: Optional['bool'] = None,
                                 scale: Optional['float'] = None,
                                 offsetX: Optional['float'] = None,
                                 offsetY: Optional['float'] = None,
                                 screenWidth: Optional['int'] = None,
                                 screenHeight: Optional['int'] = None,
                                 positionX: Optional['int'] = None,
                                 positionY: Optional['int'] = None,
                                 screenOrientation: Optional['ScreenOrientation'] = None,
                                 ):
        """Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results).
        :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :type width: int
        :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :type height: int
        :param deviceScaleFactor: Overriding device scale factor value. 0 disables the override.
        :type deviceScaleFactor: float
        :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
        :type mobile: bool
        :param fitWindow: Whether a view that exceeds the available browser window area should be scaled down to fit.
        :type fitWindow: bool
        :param scale: Scale to apply to resulting view image. Ignored in |fitWindow| mode.
        :type scale: float
        :param offsetX: Not used.
        :type offsetX: float
        :param offsetY: Not used.
        :type offsetY: float
        :param screenWidth: Overriding screen width value in pixels (minimum 0, maximum 10000000). Only used for |mobile==true|.
        :type screenWidth: int
        :param screenHeight: Overriding screen height value in pixels (minimum 0, maximum 10000000). Only used for |mobile==true|.
        :type screenHeight: int
        :param positionX: Overriding view X position on screen in pixels (minimum 0, maximum 10000000). Only used for |mobile==true|.
        :type positionX: int
        :param positionY: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000). Only used for |mobile==true|.
        :type positionY: int
        :param screenOrientation: Screen orientation override.
        :type screenOrientation: ScreenOrientation
        """
        return (
            cls.build_send_payload("setDeviceMetricsOverride", {
                "width": width,
                "height": height,
                "deviceScaleFactor": deviceScaleFactor,
                "mobile": mobile,
                "fitWindow": fitWindow,
                "scale": scale,
                "offsetX": offsetX,
                "offsetY": offsetY,
                "screenWidth": screenWidth,
                "screenHeight": screenHeight,
                "positionX": positionX,
                "positionY": positionY,
                "screenOrientation": screenOrientation,
            }),
            None
        )

    @classmethod
    def clearDeviceMetricsOverride(cls):
        """Clears the overriden device metrics.
        """
        return (
            cls.build_send_payload("clearDeviceMetricsOverride", {
            }),
            None
        )

    @classmethod
    def resetPageScaleFactor(cls):
        """Requests that page scale factor is reset to initial values.
        """
        return (
            cls.build_send_payload("resetPageScaleFactor", {
            }),
            None
        )

    @classmethod
    def setPageScaleFactor(cls,
                           pageScaleFactor: Union['float'],
                           ):
        """Sets a specified page scale factor.
        :param pageScaleFactor: Page scale factor.
        :type pageScaleFactor: float
        """
        return (
            cls.build_send_payload("setPageScaleFactor", {
                "pageScaleFactor": pageScaleFactor,
            }),
            None
        )

    @classmethod
    def setVisibleSize(cls,
                       width: Union['int'],
                       height: Union['int'],
                       ):
        """Deprecated, does nothing. Please use setDeviceMetricsOverride instead.
        :param width: Frame width (DIP).
        :type width: int
        :param height: Frame height (DIP).
        :type height: int
        """
        return (
            cls.build_send_payload("setVisibleSize", {
                "width": width,
                "height": height,
            }),
            None
        )

    @classmethod
    def setScriptExecutionDisabled(cls,
                                   value: Union['bool'],
                                   ):
        """Switches script execution in the page.
        :param value: Whether script execution should be disabled in the page.
        :type value: bool
        """
        return (
            cls.build_send_payload("setScriptExecutionDisabled", {
                "value": value,
            }),
            None
        )

    @classmethod
    def setGeolocationOverride(cls,
                               latitude: Optional['float'] = None,
                               longitude: Optional['float'] = None,
                               accuracy: Optional['float'] = None,
                               ):
        """Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position unavailable.
        :param latitude: Mock latitude
        :type latitude: float
        :param longitude: Mock longitude
        :type longitude: float
        :param accuracy: Mock accuracy
        :type accuracy: float
        """
        return (
            cls.build_send_payload("setGeolocationOverride", {
                "latitude": latitude,
                "longitude": longitude,
                "accuracy": accuracy,
            }),
            None
        )

    @classmethod
    def clearGeolocationOverride(cls):
        """Clears the overriden Geolocation Position and Error.
        """
        return (
            cls.build_send_payload("clearGeolocationOverride", {
            }),
            None
        )

    @classmethod
    def setTouchEmulationEnabled(cls,
                                 enabled: Union['bool'],
                                 configuration: Optional['str'] = None,
                                 ):
        """Toggles mouse event-based touch event emulation.
        :param enabled: Whether the touch event emulation should be enabled.
        :type enabled: bool
        :param configuration: Touch/gesture events configuration. Default: current platform.
        :type configuration: str
        """
        return (
            cls.build_send_payload("setTouchEmulationEnabled", {
                "enabled": enabled,
                "configuration": configuration,
            }),
            None
        )

    @classmethod
    def setEmulatedMedia(cls,
                         media: Union['str'],
                         ):
        """Emulates the given media for CSS media queries.
        :param media: Media type to emulate. Empty string disables the override.
        :type media: str
        """
        return (
            cls.build_send_payload("setEmulatedMedia", {
                "media": media,
            }),
            None
        )

    @classmethod
    def setCPUThrottlingRate(cls,
                             rate: Union['float'],
                             ):
        """Enables CPU throttling to emulate slow CPUs.
        :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
        :type rate: float
        """
        return (
            cls.build_send_payload("setCPUThrottlingRate", {
                "rate": rate,
            }),
            None
        )

    @classmethod
    def canEmulate(cls):
        """Tells whether emulation is supported.
        """
        return (
            cls.build_send_payload("canEmulate", {
            }),
            cls.convert_payload({
                "result": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def setVirtualTimePolicy(cls,
                             policy: Union['VirtualTimePolicy'],
                             budget: Optional['int'] = None,
                             ):
        """Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets the current virtual time policy.  Note this supersedes any previous time budget.
        :param policy: 
        :type policy: VirtualTimePolicy
        :param budget: If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent.
        :type budget: int
        """
        return (
            cls.build_send_payload("setVirtualTimePolicy", {
                "policy": policy,
                "budget": budget,
            }),
            None
        )

    @classmethod
    def setDefaultBackgroundColorOverride(cls,
                                          color: Optional['DOM.RGBA'] = None,
                                          ):
        """Sets or clears an override of the default background color of the frame. This override is used if the content does not specify one.
        :param color: RGBA of the default background color. If not specified, any existing override will be cleared.
        :type color: DOM.RGBA
        """
        return (
            cls.build_send_payload("setDefaultBackgroundColorOverride", {
                "color": color,
            }),
            None
        )



class VirtualTimeBudgetExpiredEvent(BaseEvent):

    js_name = 'Emulation.virtualTimeBudgetExpired'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
