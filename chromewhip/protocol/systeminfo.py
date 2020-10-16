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

# GPUDevice: Describes a single graphics processor (GPU).
class GPUDevice(ChromeTypeBase):
    def __init__(self,
                 vendorId: Union['float'],
                 deviceId: Union['float'],
                 vendorString: Union['str'],
                 deviceString: Union['str'],
                 driverVendor: Union['str'],
                 driverVersion: Union['str'],
                 subSysId: Optional['float'] = None,
                 revision: Optional['float'] = None,
                 ):

        self.vendorId = vendorId
        self.deviceId = deviceId
        self.subSysId = subSysId
        self.revision = revision
        self.vendorString = vendorString
        self.deviceString = deviceString
        self.driverVendor = driverVendor
        self.driverVersion = driverVersion


# Size: Describes the width and height dimensions of an entity.
class Size(ChromeTypeBase):
    def __init__(self,
                 width: Union['int'],
                 height: Union['int'],
                 ):

        self.width = width
        self.height = height


# VideoDecodeAcceleratorCapability: Describes a supported video decoding profile with its associated minimum andmaximum resolutions.
class VideoDecodeAcceleratorCapability(ChromeTypeBase):
    def __init__(self,
                 profile: Union['str'],
                 maxResolution: Union['Size'],
                 minResolution: Union['Size'],
                 ):

        self.profile = profile
        self.maxResolution = maxResolution
        self.minResolution = minResolution


# VideoEncodeAcceleratorCapability: Describes a supported video encoding profile with its associated maximumresolution and maximum framerate.
class VideoEncodeAcceleratorCapability(ChromeTypeBase):
    def __init__(self,
                 profile: Union['str'],
                 maxResolution: Union['Size'],
                 maxFramerateNumerator: Union['int'],
                 maxFramerateDenominator: Union['int'],
                 ):

        self.profile = profile
        self.maxResolution = maxResolution
        self.maxFramerateNumerator = maxFramerateNumerator
        self.maxFramerateDenominator = maxFramerateDenominator


# SubsamplingFormat: YUV subsampling type of the pixels of a given image.
SubsamplingFormat = str

# ImageType: Image format of a given image.
ImageType = str

# ImageDecodeAcceleratorCapability: Describes a supported image decoding profile with its associated minimum andmaximum resolutions and subsampling.
class ImageDecodeAcceleratorCapability(ChromeTypeBase):
    def __init__(self,
                 imageType: Union['ImageType'],
                 maxDimensions: Union['Size'],
                 minDimensions: Union['Size'],
                 subsamplings: Union['[SubsamplingFormat]'],
                 ):

        self.imageType = imageType
        self.maxDimensions = maxDimensions
        self.minDimensions = minDimensions
        self.subsamplings = subsamplings


# GPUInfo: Provides information about the GPU(s) on the system.
class GPUInfo(ChromeTypeBase):
    def __init__(self,
                 devices: Union['[GPUDevice]'],
                 driverBugWorkarounds: Union['[]'],
                 videoDecoding: Union['[VideoDecodeAcceleratorCapability]'],
                 videoEncoding: Union['[VideoEncodeAcceleratorCapability]'],
                 imageDecoding: Union['[ImageDecodeAcceleratorCapability]'],
                 auxAttributes: Optional['dict'] = None,
                 featureStatus: Optional['dict'] = None,
                 ):

        self.devices = devices
        self.auxAttributes = auxAttributes
        self.featureStatus = featureStatus
        self.driverBugWorkarounds = driverBugWorkarounds
        self.videoDecoding = videoDecoding
        self.videoEncoding = videoEncoding
        self.imageDecoding = imageDecoding


# ProcessInfo: Represents process info.
class ProcessInfo(ChromeTypeBase):
    def __init__(self,
                 type: Union['str'],
                 id: Union['int'],
                 cpuTime: Union['float'],
                 ):

        self.type = type
        self.id = id
        self.cpuTime = cpuTime


class SystemInfo(PayloadMixin):
    """ The SystemInfo domain defines methods and events for querying low-level system information.
    """
    @classmethod
    def getInfo(cls):
        """Returns information about the system.
        """
        return (
            cls.build_send_payload("getInfo", {
            }),
            cls.convert_payload({
                "gpu": {
                    "class": GPUInfo,
                    "optional": False
                },
                "modelName": {
                    "class": str,
                    "optional": False
                },
                "modelVersion": {
                    "class": str,
                    "optional": False
                },
                "commandLine": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def getProcessInfo(cls):
        """Returns information about all running processes.
        """
        return (
            cls.build_send_payload("getProcessInfo", {
            }),
            cls.convert_payload({
                "processInfo": {
                    "class": [ProcessInfo],
                    "optional": False
                },
            })
        )

