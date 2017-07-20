# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import debugger as Debugger
from chromewhip.protocol import dom as DOM
from chromewhip.protocol import network as Network
from chromewhip.protocol import runtime as Runtime
from chromewhip.protocol import emulation as Emulation

# ResourceType: Resource type as it was perceived by the rendering engine.
ResourceType = str

# FrameId: Unique frame identifier.
FrameId = str

# Frame: Information about the Frame on the page.
class Frame(ChromeTypeBase):
    def __init__(self,
                 id: Union['str'],
                 loaderId: Union['Network.LoaderId'],
                 url: Union['str'],
                 securityOrigin: Union['str'],
                 mimeType: Union['str'],
                 parentId: Optional['str'] = None,
                 name: Optional['str'] = None,
                 unreachableUrl: Optional['str'] = None,
                 ):

        self.id = id
        self.parentId = parentId
        self.loaderId = loaderId
        self.name = name
        self.url = url
        self.securityOrigin = securityOrigin
        self.mimeType = mimeType
        self.unreachableUrl = unreachableUrl


# FrameResource: Information about the Resource on the page.
class FrameResource(ChromeTypeBase):
    def __init__(self,
                 url: Union['str'],
                 type: Union['ResourceType'],
                 mimeType: Union['str'],
                 lastModified: Optional['Network.TimeSinceEpoch'] = None,
                 contentSize: Optional['float'] = None,
                 failed: Optional['bool'] = None,
                 canceled: Optional['bool'] = None,
                 ):

        self.url = url
        self.type = type
        self.mimeType = mimeType
        self.lastModified = lastModified
        self.contentSize = contentSize
        self.failed = failed
        self.canceled = canceled


# FrameResourceTree: Information about the Frame hierarchy along with their cached resources.
class FrameResourceTree(ChromeTypeBase):
    def __init__(self,
                 frame: Union['Frame'],
                 resources: Union['[FrameResource]'],
                 childFrames: Optional['[FrameResourceTree]'] = None,
                 ):

        self.frame = frame
        self.childFrames = childFrames
        self.resources = resources


# ScriptIdentifier: Unique script identifier.
ScriptIdentifier = str

# TransitionType: Transition type.
TransitionType = str

# NavigationEntry: Navigation history entry.
class NavigationEntry(ChromeTypeBase):
    def __init__(self,
                 id: Union['int'],
                 url: Union['str'],
                 userTypedURL: Union['str'],
                 title: Union['str'],
                 transitionType: Union['TransitionType'],
                 ):

        self.id = id
        self.url = url
        self.userTypedURL = userTypedURL
        self.title = title
        self.transitionType = transitionType


# ScreencastFrameMetadata: Screencast frame metadata.
class ScreencastFrameMetadata(ChromeTypeBase):
    def __init__(self,
                 offsetTop: Union['float'],
                 pageScaleFactor: Union['float'],
                 deviceWidth: Union['float'],
                 deviceHeight: Union['float'],
                 scrollOffsetX: Union['float'],
                 scrollOffsetY: Union['float'],
                 timestamp: Optional['Network.TimeSinceEpoch'] = None,
                 ):

        self.offsetTop = offsetTop
        self.pageScaleFactor = pageScaleFactor
        self.deviceWidth = deviceWidth
        self.deviceHeight = deviceHeight
        self.scrollOffsetX = scrollOffsetX
        self.scrollOffsetY = scrollOffsetY
        self.timestamp = timestamp


# DialogType: Javascript dialog type.
DialogType = str

# AppManifestError: Error while paring app manifest.
class AppManifestError(ChromeTypeBase):
    def __init__(self,
                 message: Union['str'],
                 critical: Union['int'],
                 line: Union['int'],
                 column: Union['int'],
                 ):

        self.message = message
        self.critical = critical
        self.line = line
        self.column = column


# NavigationResponse: Proceed: allow the navigation; Cancel: cancel the navigation; CancelAndIgnore: cancels the navigation and makes the requester of the navigation acts like the request was never made.
NavigationResponse = str

# LayoutViewport: Layout viewport position and dimensions.
class LayoutViewport(ChromeTypeBase):
    def __init__(self,
                 pageX: Union['int'],
                 pageY: Union['int'],
                 clientWidth: Union['int'],
                 clientHeight: Union['int'],
                 ):

        self.pageX = pageX
        self.pageY = pageY
        self.clientWidth = clientWidth
        self.clientHeight = clientHeight


# VisualViewport: Visual viewport position, dimensions, and scale.
class VisualViewport(ChromeTypeBase):
    def __init__(self,
                 offsetX: Union['float'],
                 offsetY: Union['float'],
                 pageX: Union['float'],
                 pageY: Union['float'],
                 clientWidth: Union['float'],
                 clientHeight: Union['float'],
                 scale: Union['float'],
                 ):

        self.offsetX = offsetX
        self.offsetY = offsetY
        self.pageX = pageX
        self.pageY = pageY
        self.clientWidth = clientWidth
        self.clientHeight = clientHeight
        self.scale = scale


# Viewport: Viewport for capturing screenshot.
class Viewport(ChromeTypeBase):
    def __init__(self,
                 x: Union['float'],
                 y: Union['float'],
                 width: Union['float'],
                 height: Union['float'],
                 scale: Union['float'],
                 ):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = scale


class Page(PayloadMixin):
    """ Actions and events related to the inspected page belong to the page domain.
    """
    @classmethod
    def enable(cls):
        """Enables page domain notifications.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables page domain notifications.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def addScriptToEvaluateOnLoad(cls,
                                  scriptSource: Union['str'],
                                  ):
        """Deprecated, please use addScriptToEvaluateOnNewDocument instead.
        :param scriptSource: 
        :type scriptSource: str
        """
        return (
            cls.build_send_payload("addScriptToEvaluateOnLoad", {
                "scriptSource": scriptSource,
            }),
            cls.convert_payload({
                "identifier": {
                    "class": ScriptIdentifier,
                    "optional": False
                },
            })
        )

    @classmethod
    def removeScriptToEvaluateOnLoad(cls,
                                     identifier: Union['ScriptIdentifier'],
                                     ):
        """Deprecated, please use removeScriptToEvaluateOnNewDocument instead.
        :param identifier: 
        :type identifier: ScriptIdentifier
        """
        return (
            cls.build_send_payload("removeScriptToEvaluateOnLoad", {
                "identifier": identifier,
            }),
            None
        )

    @classmethod
    def addScriptToEvaluateOnNewDocument(cls,
                                         source: Union['str'],
                                         ):
        """Evaluates given script in every frame upon creation (before loading frame's scripts).
        :param source: 
        :type source: str
        """
        return (
            cls.build_send_payload("addScriptToEvaluateOnNewDocument", {
                "source": source,
            }),
            cls.convert_payload({
                "identifier": {
                    "class": ScriptIdentifier,
                    "optional": False
                },
            })
        )

    @classmethod
    def removeScriptToEvaluateOnNewDocument(cls,
                                            identifier: Union['ScriptIdentifier'],
                                            ):
        """Removes given script from the list.
        :param identifier: 
        :type identifier: ScriptIdentifier
        """
        return (
            cls.build_send_payload("removeScriptToEvaluateOnNewDocument", {
                "identifier": identifier,
            }),
            None
        )

    @classmethod
    def setAutoAttachToCreatedPages(cls,
                                    autoAttach: Union['bool'],
                                    ):
        """Controls whether browser will open a new inspector window for connected pages.
        :param autoAttach: If true, browser will open a new inspector window for every page created from this one.
        :type autoAttach: bool
        """
        return (
            cls.build_send_payload("setAutoAttachToCreatedPages", {
                "autoAttach": autoAttach,
            }),
            None
        )

    @classmethod
    def reload(cls,
               ignoreCache: Optional['bool'] = None,
               scriptToEvaluateOnLoad: Optional['str'] = None,
               ):
        """Reloads given page optionally ignoring the cache.
        :param ignoreCache: If true, browser cache is ignored (as if the user pressed Shift+refresh).
        :type ignoreCache: bool
        :param scriptToEvaluateOnLoad: If set, the script will be injected into all frames of the inspected page after reload.
        :type scriptToEvaluateOnLoad: str
        """
        return (
            cls.build_send_payload("reload", {
                "ignoreCache": ignoreCache,
                "scriptToEvaluateOnLoad": scriptToEvaluateOnLoad,
            }),
            None
        )

    @classmethod
    def navigate(cls,
                 url: Union['str'],
                 referrer: Optional['str'] = None,
                 transitionType: Optional['TransitionType'] = None,
                 ):
        """Navigates current page to the given URL.
        :param url: URL to navigate the page to.
        :type url: str
        :param referrer: Referrer URL.
        :type referrer: str
        :param transitionType: Intended transition type.
        :type transitionType: TransitionType
        """
        return (
            cls.build_send_payload("navigate", {
                "url": url,
                "referrer": referrer,
                "transitionType": transitionType,
            }),
            cls.convert_payload({
                "frameId": {
                    "class": FrameId,
                    "optional": False
                },
            })
        )

    @classmethod
    def stopLoading(cls):
        """Force the page stop all navigations and pending resource fetches.
        """
        return (
            cls.build_send_payload("stopLoading", {
            }),
            None
        )

    @classmethod
    def getNavigationHistory(cls):
        """Returns navigation history for the current page.
        """
        return (
            cls.build_send_payload("getNavigationHistory", {
            }),
            cls.convert_payload({
                "currentIndex": {
                    "class": int,
                    "optional": False
                },
                "entries": {
                    "class": [NavigationEntry],
                    "optional": False
                },
            })
        )

    @classmethod
    def navigateToHistoryEntry(cls,
                               entryId: Union['int'],
                               ):
        """Navigates current page to the given history entry.
        :param entryId: Unique id of the entry to navigate to.
        :type entryId: int
        """
        return (
            cls.build_send_payload("navigateToHistoryEntry", {
                "entryId": entryId,
            }),
            None
        )

    @classmethod
    def getCookies(cls):
        """Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field.
        """
        return (
            cls.build_send_payload("getCookies", {
            }),
            cls.convert_payload({
                "cookies": {
                    "class": [Network.Cookie],
                    "optional": False
                },
            })
        )

    @classmethod
    def deleteCookie(cls,
                     cookieName: Union['str'],
                     url: Union['str'],
                     ):
        """Deletes browser cookie with given name, domain and path.
        :param cookieName: Name of the cookie to remove.
        :type cookieName: str
        :param url: URL to match cooke domain and path.
        :type url: str
        """
        return (
            cls.build_send_payload("deleteCookie", {
                "cookieName": cookieName,
                "url": url,
            }),
            None
        )

    @classmethod
    def getResourceTree(cls):
        """Returns present frame / resource tree structure.
        """
        return (
            cls.build_send_payload("getResourceTree", {
            }),
            cls.convert_payload({
                "frameTree": {
                    "class": FrameResourceTree,
                    "optional": False
                },
            })
        )

    @classmethod
    def getResourceContent(cls,
                           frameId: Union['FrameId'],
                           url: Union['str'],
                           ):
        """Returns content of the given resource.
        :param frameId: Frame id to get resource for.
        :type frameId: FrameId
        :param url: URL of the resource to get content for.
        :type url: str
        """
        return (
            cls.build_send_payload("getResourceContent", {
                "frameId": frameId,
                "url": url,
            }),
            cls.convert_payload({
                "content": {
                    "class": str,
                    "optional": False
                },
                "base64Encoded": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def searchInResource(cls,
                         frameId: Union['FrameId'],
                         url: Union['str'],
                         query: Union['str'],
                         caseSensitive: Optional['bool'] = None,
                         isRegex: Optional['bool'] = None,
                         ):
        """Searches for given string in resource content.
        :param frameId: Frame id for resource to search in.
        :type frameId: FrameId
        :param url: URL of the resource to search in.
        :type url: str
        :param query: String to search for.
        :type query: str
        :param caseSensitive: If true, search is case sensitive.
        :type caseSensitive: bool
        :param isRegex: If true, treats string parameter as regex.
        :type isRegex: bool
        """
        return (
            cls.build_send_payload("searchInResource", {
                "frameId": frameId,
                "url": url,
                "query": query,
                "caseSensitive": caseSensitive,
                "isRegex": isRegex,
            }),
            cls.convert_payload({
                "result": {
                    "class": [Debugger.SearchMatch],
                    "optional": False
                },
            })
        )

    @classmethod
    def setDocumentContent(cls,
                           frameId: Union['FrameId'],
                           html: Union['str'],
                           ):
        """Sets given markup as the document's HTML.
        :param frameId: Frame id to set HTML for.
        :type frameId: FrameId
        :param html: HTML content to set.
        :type html: str
        """
        return (
            cls.build_send_payload("setDocumentContent", {
                "frameId": frameId,
                "html": html,
            }),
            None
        )

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
                                 screenOrientation: Optional['Emulation.ScreenOrientation'] = None,
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
        :param offsetX: X offset to shift resulting view image by. Ignored in |fitWindow| mode.
        :type offsetX: float
        :param offsetY: Y offset to shift resulting view image by. Ignored in |fitWindow| mode.
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
        :type screenOrientation: Emulation.ScreenOrientation
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
    def setDeviceOrientationOverride(cls,
                                     alpha: Union['float'],
                                     beta: Union['float'],
                                     gamma: Union['float'],
                                     ):
        """Overrides the Device Orientation.
        :param alpha: Mock alpha
        :type alpha: float
        :param beta: Mock beta
        :type beta: float
        :param gamma: Mock gamma
        :type gamma: float
        """
        return (
            cls.build_send_payload("setDeviceOrientationOverride", {
                "alpha": alpha,
                "beta": beta,
                "gamma": gamma,
            }),
            None
        )

    @classmethod
    def clearDeviceOrientationOverride(cls):
        """Clears the overridden Device Orientation.
        """
        return (
            cls.build_send_payload("clearDeviceOrientationOverride", {
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
    def captureScreenshot(cls,
                          format: Optional['str'] = None,
                          quality: Optional['int'] = None,
                          clip: Optional['Viewport'] = None,
                          fromSurface: Optional['bool'] = None,
                          ):
        """Capture page screenshot.
        :param format: Image compression format (defaults to png).
        :type format: str
        :param quality: Compression quality from range [0..100] (jpeg only).
        :type quality: int
        :param clip: Capture the screenshot of a given region only.
        :type clip: Viewport
        :param fromSurface: Capture the screenshot from the surface, rather than the view. Defaults to true.
        :type fromSurface: bool
        """
        return (
            cls.build_send_payload("captureScreenshot", {
                "format": format,
                "quality": quality,
                "clip": clip,
                "fromSurface": fromSurface,
            }),
            cls.convert_payload({
                "data": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def printToPDF(cls,
                   landscape: Optional['bool'] = None,
                   displayHeaderFooter: Optional['bool'] = None,
                   printBackground: Optional['bool'] = None,
                   scale: Optional['float'] = None,
                   paperWidth: Optional['float'] = None,
                   paperHeight: Optional['float'] = None,
                   marginTop: Optional['float'] = None,
                   marginBottom: Optional['float'] = None,
                   marginLeft: Optional['float'] = None,
                   marginRight: Optional['float'] = None,
                   pageRanges: Optional['str'] = None,
                   ignoreInvalidPageRanges: Optional['bool'] = None,
                   ):
        """Print page as PDF.
        :param landscape: Paper orientation. Defaults to false.
        :type landscape: bool
        :param displayHeaderFooter: Display header and footer. Defaults to false.
        :type displayHeaderFooter: bool
        :param printBackground: Print background graphics. Defaults to false.
        :type printBackground: bool
        :param scale: Scale of the webpage rendering. Defaults to 1.
        :type scale: float
        :param paperWidth: Paper width in inches. Defaults to 8.5 inches.
        :type paperWidth: float
        :param paperHeight: Paper height in inches. Defaults to 11 inches.
        :type paperHeight: float
        :param marginTop: Top margin in inches. Defaults to 1cm (~0.4 inches).
        :type marginTop: float
        :param marginBottom: Bottom margin in inches. Defaults to 1cm (~0.4 inches).
        :type marginBottom: float
        :param marginLeft: Left margin in inches. Defaults to 1cm (~0.4 inches).
        :type marginLeft: float
        :param marginRight: Right margin in inches. Defaults to 1cm (~0.4 inches).
        :type marginRight: float
        :param pageRanges: Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.
        :type pageRanges: str
        :param ignoreInvalidPageRanges: Whether to silently ignore invalid but successfully parsed page ranges, such as '3-2'. Defaults to false.
        :type ignoreInvalidPageRanges: bool
        """
        return (
            cls.build_send_payload("printToPDF", {
                "landscape": landscape,
                "displayHeaderFooter": displayHeaderFooter,
                "printBackground": printBackground,
                "scale": scale,
                "paperWidth": paperWidth,
                "paperHeight": paperHeight,
                "marginTop": marginTop,
                "marginBottom": marginBottom,
                "marginLeft": marginLeft,
                "marginRight": marginRight,
                "pageRanges": pageRanges,
                "ignoreInvalidPageRanges": ignoreInvalidPageRanges,
            }),
            cls.convert_payload({
                "data": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def startScreencast(cls,
                        format: Optional['str'] = None,
                        quality: Optional['int'] = None,
                        maxWidth: Optional['int'] = None,
                        maxHeight: Optional['int'] = None,
                        everyNthFrame: Optional['int'] = None,
                        ):
        """Starts sending each frame using the <code>screencastFrame</code> event.
        :param format: Image compression format.
        :type format: str
        :param quality: Compression quality from range [0..100].
        :type quality: int
        :param maxWidth: Maximum screenshot width.
        :type maxWidth: int
        :param maxHeight: Maximum screenshot height.
        :type maxHeight: int
        :param everyNthFrame: Send every n-th frame.
        :type everyNthFrame: int
        """
        return (
            cls.build_send_payload("startScreencast", {
                "format": format,
                "quality": quality,
                "maxWidth": maxWidth,
                "maxHeight": maxHeight,
                "everyNthFrame": everyNthFrame,
            }),
            None
        )

    @classmethod
    def stopScreencast(cls):
        """Stops sending each frame in the <code>screencastFrame</code>.
        """
        return (
            cls.build_send_payload("stopScreencast", {
            }),
            None
        )

    @classmethod
    def screencastFrameAck(cls,
                           sessionId: Union['int'],
                           ):
        """Acknowledges that a screencast frame has been received by the frontend.
        :param sessionId: Frame number.
        :type sessionId: int
        """
        return (
            cls.build_send_payload("screencastFrameAck", {
                "sessionId": sessionId,
            }),
            None
        )

    @classmethod
    def handleJavaScriptDialog(cls,
                               accept: Union['bool'],
                               promptText: Optional['str'] = None,
                               ):
        """Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).
        :param accept: Whether to accept or dismiss the dialog.
        :type accept: bool
        :param promptText: The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog.
        :type promptText: str
        """
        return (
            cls.build_send_payload("handleJavaScriptDialog", {
                "accept": accept,
                "promptText": promptText,
            }),
            None
        )

    @classmethod
    def getAppManifest(cls):
        """
        """
        return (
            cls.build_send_payload("getAppManifest", {
            }),
            cls.convert_payload({
                "url": {
                    "class": str,
                    "optional": False
                },
                "errors": {
                    "class": [AppManifestError],
                    "optional": False
                },
                "data": {
                    "class": str,
                    "optional": True
                },
            })
        )

    @classmethod
    def requestAppBanner(cls):
        """
        """
        return (
            cls.build_send_payload("requestAppBanner", {
            }),
            None
        )

    @classmethod
    def setControlNavigations(cls,
                              enabled: Union['bool'],
                              ):
        """Toggles navigation throttling which allows programatic control over navigation and redirect response.
        :param enabled: 
        :type enabled: bool
        """
        return (
            cls.build_send_payload("setControlNavigations", {
                "enabled": enabled,
            }),
            None
        )

    @classmethod
    def processNavigation(cls,
                          response: Union['NavigationResponse'],
                          navigationId: Union['int'],
                          ):
        """Should be sent in response to a navigationRequested or a redirectRequested event, telling the browser how to handle the navigation.
        :param response: 
        :type response: NavigationResponse
        :param navigationId: 
        :type navigationId: int
        """
        return (
            cls.build_send_payload("processNavigation", {
                "response": response,
                "navigationId": navigationId,
            }),
            None
        )

    @classmethod
    def getLayoutMetrics(cls):
        """Returns metrics relating to the layouting of the page, such as viewport bounds/scale.
        """
        return (
            cls.build_send_payload("getLayoutMetrics", {
            }),
            cls.convert_payload({
                "layoutViewport": {
                    "class": LayoutViewport,
                    "optional": False
                },
                "visualViewport": {
                    "class": VisualViewport,
                    "optional": False
                },
                "contentSize": {
                    "class": DOM.Rect,
                    "optional": False
                },
            })
        )

    @classmethod
    def createIsolatedWorld(cls,
                            frameId: Union['FrameId'],
                            worldName: Optional['str'] = None,
                            grantUniveralAccess: Optional['bool'] = None,
                            ):
        """Creates an isolated world for the given frame.
        :param frameId: Id of the frame in which the isolated world should be created.
        :type frameId: FrameId
        :param worldName: An optional name which is reported in the Execution Context.
        :type worldName: str
        :param grantUniveralAccess: Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution.
        :type grantUniveralAccess: bool
        """
        return (
            cls.build_send_payload("createIsolatedWorld", {
                "frameId": frameId,
                "worldName": worldName,
                "grantUniveralAccess": grantUniveralAccess,
            }),
            cls.convert_payload({
                "executionContextId": {
                    "class": Runtime.ExecutionContextId,
                    "optional": False
                },
            })
        )



class DomContentEventFiredEvent(BaseEvent):

    js_name = 'Page.domContentEventFired'
    hashable = []
    is_hashable = False

    def __init__(self,
                 timestamp: Union['Network.MonotonicTime', dict],
                 ):
        if isinstance(timestamp, dict):
            timestamp = Network.MonotonicTime(**timestamp)
        self.timestamp = timestamp

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class LoadEventFiredEvent(BaseEvent):

    js_name = 'Page.loadEventFired'
    hashable = []
    is_hashable = False

    def __init__(self,
                 timestamp: Union['Network.MonotonicTime', dict],
                 ):
        if isinstance(timestamp, dict):
            timestamp = Network.MonotonicTime(**timestamp)
        self.timestamp = timestamp

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class FrameAttachedEvent(BaseEvent):

    js_name = 'Page.frameAttached'
    hashable = ['frameId', 'parentFrameId']
    is_hashable = True

    def __init__(self,
                 frameId: Union['FrameId', dict],
                 parentFrameId: Union['FrameId', dict],
                 stack: Union['Runtime.StackTrace', dict, None] = None,
                 ):
        if isinstance(frameId, dict):
            frameId = FrameId(**frameId)
        self.frameId = frameId
        if isinstance(parentFrameId, dict):
            parentFrameId = FrameId(**parentFrameId)
        self.parentFrameId = parentFrameId
        if isinstance(stack, dict):
            stack = Runtime.StackTrace(**stack)
        self.stack = stack

    @classmethod
    def build_hash(cls, frameId, parentFrameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class FrameNavigatedEvent(BaseEvent):

    js_name = 'Page.frameNavigated'
    hashable = ['frameId']
    is_hashable = True

    def __init__(self,
                 frame: Union['Frame', dict],
                 ):
        if isinstance(frame, dict):
            frame = Frame(**frame)
        self.frame = frame

    @classmethod
    def build_hash(cls, frameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class FrameDetachedEvent(BaseEvent):

    js_name = 'Page.frameDetached'
    hashable = ['frameId']
    is_hashable = True

    def __init__(self,
                 frameId: Union['FrameId', dict],
                 ):
        if isinstance(frameId, dict):
            frameId = FrameId(**frameId)
        self.frameId = frameId

    @classmethod
    def build_hash(cls, frameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class FrameStartedLoadingEvent(BaseEvent):

    js_name = 'Page.frameStartedLoading'
    hashable = ['frameId']
    is_hashable = True

    def __init__(self,
                 frameId: Union['FrameId', dict],
                 ):
        if isinstance(frameId, dict):
            frameId = FrameId(**frameId)
        self.frameId = frameId

    @classmethod
    def build_hash(cls, frameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class FrameStoppedLoadingEvent(BaseEvent):

    js_name = 'Page.frameStoppedLoading'
    hashable = ['frameId']
    is_hashable = True

    def __init__(self,
                 frameId: Union['FrameId', dict],
                 ):
        if isinstance(frameId, dict):
            frameId = FrameId(**frameId)
        self.frameId = frameId

    @classmethod
    def build_hash(cls, frameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class FrameScheduledNavigationEvent(BaseEvent):

    js_name = 'Page.frameScheduledNavigation'
    hashable = ['frameId']
    is_hashable = True

    def __init__(self,
                 frameId: Union['FrameId', dict],
                 delay: Union['float', dict],
                 ):
        if isinstance(frameId, dict):
            frameId = FrameId(**frameId)
        self.frameId = frameId
        if isinstance(delay, dict):
            delay = float(**delay)
        self.delay = delay

    @classmethod
    def build_hash(cls, frameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class FrameClearedScheduledNavigationEvent(BaseEvent):

    js_name = 'Page.frameClearedScheduledNavigation'
    hashable = ['frameId']
    is_hashable = True

    def __init__(self,
                 frameId: Union['FrameId', dict],
                 ):
        if isinstance(frameId, dict):
            frameId = FrameId(**frameId)
        self.frameId = frameId

    @classmethod
    def build_hash(cls, frameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class FrameResizedEvent(BaseEvent):

    js_name = 'Page.frameResized'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class JavascriptDialogOpeningEvent(BaseEvent):

    js_name = 'Page.javascriptDialogOpening'
    hashable = []
    is_hashable = False

    def __init__(self,
                 message: Union['str', dict],
                 type: Union['DialogType', dict],
                 ):
        if isinstance(message, dict):
            message = str(**message)
        self.message = message
        if isinstance(type, dict):
            type = DialogType(**type)
        self.type = type

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class JavascriptDialogClosedEvent(BaseEvent):

    js_name = 'Page.javascriptDialogClosed'
    hashable = []
    is_hashable = False

    def __init__(self,
                 result: Union['bool', dict],
                 ):
        if isinstance(result, dict):
            result = bool(**result)
        self.result = result

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class ScreencastFrameEvent(BaseEvent):

    js_name = 'Page.screencastFrame'
    hashable = ['sessionId']
    is_hashable = True

    def __init__(self,
                 data: Union['str', dict],
                 metadata: Union['ScreencastFrameMetadata', dict],
                 sessionId: Union['int', dict],
                 ):
        if isinstance(data, dict):
            data = str(**data)
        self.data = data
        if isinstance(metadata, dict):
            metadata = ScreencastFrameMetadata(**metadata)
        self.metadata = metadata
        if isinstance(sessionId, dict):
            sessionId = int(**sessionId)
        self.sessionId = sessionId

    @classmethod
    def build_hash(cls, sessionId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class ScreencastVisibilityChangedEvent(BaseEvent):

    js_name = 'Page.screencastVisibilityChanged'
    hashable = []
    is_hashable = False

    def __init__(self,
                 visible: Union['bool', dict],
                 ):
        if isinstance(visible, dict):
            visible = bool(**visible)
        self.visible = visible

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class InterstitialShownEvent(BaseEvent):

    js_name = 'Page.interstitialShown'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class InterstitialHiddenEvent(BaseEvent):

    js_name = 'Page.interstitialHidden'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class NavigationRequestedEvent(BaseEvent):

    js_name = 'Page.navigationRequested'
    hashable = ['navigationId']
    is_hashable = True

    def __init__(self,
                 isInMainFrame: Union['bool', dict],
                 isRedirect: Union['bool', dict],
                 navigationId: Union['int', dict],
                 url: Union['str', dict],
                 ):
        if isinstance(isInMainFrame, dict):
            isInMainFrame = bool(**isInMainFrame)
        self.isInMainFrame = isInMainFrame
        if isinstance(isRedirect, dict):
            isRedirect = bool(**isRedirect)
        self.isRedirect = isRedirect
        if isinstance(navigationId, dict):
            navigationId = int(**navigationId)
        self.navigationId = navigationId
        if isinstance(url, dict):
            url = str(**url)
        self.url = url

    @classmethod
    def build_hash(cls, navigationId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
