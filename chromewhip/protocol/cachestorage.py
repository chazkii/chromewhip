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

# CacheId: Unique identifier of the Cache object.
CacheId = str

# CachedResponseType: type of HTTP response cached
CachedResponseType = str

# DataEntry: Data entry.
class DataEntry(ChromeTypeBase):
    def __init__(self,
                 requestURL: Union['str'],
                 requestMethod: Union['str'],
                 requestHeaders: Union['[Header]'],
                 responseTime: Union['float'],
                 responseStatus: Union['int'],
                 responseStatusText: Union['str'],
                 responseType: Union['CachedResponseType'],
                 responseHeaders: Union['[Header]'],
                 ):

        self.requestURL = requestURL
        self.requestMethod = requestMethod
        self.requestHeaders = requestHeaders
        self.responseTime = responseTime
        self.responseStatus = responseStatus
        self.responseStatusText = responseStatusText
        self.responseType = responseType
        self.responseHeaders = responseHeaders


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


# Header: 
class Header(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['str'],
                 ):

        self.name = name
        self.value = value


# CachedResponse: Cached response
class CachedResponse(ChromeTypeBase):
    def __init__(self,
                 body: Union['str'],
                 ):

        self.body = body


class CacheStorage(PayloadMixin):
    """ 
    """
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
    def requestCachedResponse(cls,
                              cacheId: Union['CacheId'],
                              requestURL: Union['str'],
                              requestHeaders: Union['[Header]'],
                              ):
        """Fetches cache entry.
        :param cacheId: Id of cache that contains the entry.
        :type cacheId: CacheId
        :param requestURL: URL spec of the request.
        :type requestURL: str
        :param requestHeaders: headers of the request.
        :type requestHeaders: [Header]
        """
        return (
            cls.build_send_payload("requestCachedResponse", {
                "cacheId": cacheId,
                "requestURL": requestURL,
                "requestHeaders": requestHeaders,
            }),
            cls.convert_payload({
                "response": {
                    "class": CachedResponse,
                    "optional": False
                },
            })
        )

    @classmethod
    def requestEntries(cls,
                       cacheId: Union['CacheId'],
                       skipCount: Optional['int'] = None,
                       pageSize: Optional['int'] = None,
                       pathFilter: Optional['str'] = None,
                       ):
        """Requests data from cache.
        :param cacheId: ID of cache to get entries from.
        :type cacheId: CacheId
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        :param pathFilter: If present, only return the entries containing this substring in the path
        :type pathFilter: str
        """
        return (
            cls.build_send_payload("requestEntries", {
                "cacheId": cacheId,
                "skipCount": skipCount,
                "pageSize": pageSize,
                "pathFilter": pathFilter,
            }),
            cls.convert_payload({
                "cacheDataEntries": {
                    "class": [DataEntry],
                    "optional": False
                },
                "returnCount": {
                    "class": float,
                    "optional": False
                },
            })
        )

