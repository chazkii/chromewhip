# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# StorageType: Enum of possible storage types.
StorageType = str

# UsageForType: Usage for a storage type.
class UsageForType(ChromeTypeBase):
    def __init__(self,
                 storageType: Union['StorageType'],
                 usage: Union['float'],
                 ):

        self.storageType = storageType
        self.usage = usage


class Storage(PayloadMixin):
    """ 
    """
    @classmethod
    def clearDataForOrigin(cls,
                           origin: Union['str'],
                           storageTypes: Union['str'],
                           ):
        """Clears storage for origin.
        :param origin: Security origin.
        :type origin: str
        :param storageTypes: Comma separated origin names.
        :type storageTypes: str
        """
        return (
            cls.build_send_payload("clearDataForOrigin", {
                "origin": origin,
                "storageTypes": storageTypes,
            }),
            None
        )

    @classmethod
    def getUsageAndQuota(cls,
                         origin: Union['str'],
                         ):
        """Returns usage and quota in bytes.
        :param origin: Security origin.
        :type origin: str
        """
        return (
            cls.build_send_payload("getUsageAndQuota", {
                "origin": origin,
            }),
            cls.convert_payload({
                "usage": {
                    "class": float,
                    "optional": False
                },
                "quota": {
                    "class": float,
                    "optional": False
                },
                "usageBreakdown": {
                    "class": [UsageForType],
                    "optional": False
                },
            })
        )

