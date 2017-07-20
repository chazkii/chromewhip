# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# CacheId: Unique identifier of the Cache object.
CacheId = str

# DataEntry: Data entry.
class DataEntry(ChromeTypeBase):
    def __init__(self,
                 request: Union['str'],
                 response: Union['str'],
                 responseTime: Union['float'],
                 ):

        self.request = request
        self.response = response
        self.responseTime = responseTime


# Cache: Cache identifier.
class Cache(ChromeTypeBase):
    def __init__(self,
                 cacheId: Union['CacheId'],
                 securityOrigin: Union['str'],
                 cacheName: Union['str'],
                 ):

        self.cacheId = cacheId
        self.securityOrigin = securityOrigin
        self.cacheName = cacheName


class CacheStorage(PayloadMixin):
    """ 
    """
    @classmethod
    def requestCacheNames(cls,
                          securityOrigin: Union['str'],
                          ):
        """Requests cache names.
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        return (
            cls.build_send_payload("requestCacheNames", {
                "securityOrigin": securityOrigin,
            }),
            cls.convert_payload({
                "caches": {
                    "class": [Cache],
                    "optional": False
                },
            })
        )

    @classmethod
    def requestEntries(cls,
                       cacheId: Union['CacheId'],
                       skipCount: Union['int'],
                       pageSize: Union['int'],
                       ):
        """Requests data from cache.
        :param cacheId: ID of cache to get entries from.
        :type cacheId: CacheId
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        """
        return (
            cls.build_send_payload("requestEntries", {
                "cacheId": cacheId,
                "skipCount": skipCount,
                "pageSize": pageSize,
            }),
            cls.convert_payload({
                "cacheDataEntries": {
                    "class": [DataEntry],
                    "optional": False
                },
                "hasMore": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def deleteCache(cls,
                    cacheId: Union['CacheId'],
                    ):
        """Deletes a cache.
        :param cacheId: Id of cache for deletion.
        :type cacheId: CacheId
        """
        return (
            cls.build_send_payload("deleteCache", {
                "cacheId": cacheId,
            }),
            None
        )

    @classmethod
    def deleteEntry(cls,
                    cacheId: Union['CacheId'],
                    request: Union['str'],
                    ):
        """Deletes a cache entry.
        :param cacheId: Id of cache where the entry will be deleted.
        :type cacheId: CacheId
        :param request: URL spec of the request.
        :type request: str
        """
        return (
            cls.build_send_payload("deleteEntry", {
                "cacheId": cacheId,
                "request": request,
            }),
            None
        )

