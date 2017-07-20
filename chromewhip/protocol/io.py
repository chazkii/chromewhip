# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# StreamHandle: 
StreamHandle = str

class IO(PayloadMixin):
    """ Input/Output operations for streams produced by DevTools.
    """
    @classmethod
    def read(cls,
             handle: Union['StreamHandle'],
             offset: Optional['int'] = None,
             size: Optional['int'] = None,
             ):
        """Read a chunk of the stream
        :param handle: Handle of the stream to read.
        :type handle: StreamHandle
        :param offset: Seek to the specified offset before reading (if not specificed, proceed with offset following the last read).
        :type offset: int
        :param size: Maximum number of bytes to read (left upon the agent discretion if not specified).
        :type size: int
        """
        return (
            cls.build_send_payload("read", {
                "handle": handle,
                "offset": offset,
                "size": size,
            }),
            cls.convert_payload({
                "data": {
                    "class": str,
                    "optional": False
                },
                "eof": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def close(cls,
              handle: Union['StreamHandle'],
              ):
        """Close the stream, discard any temporary backing storage.
        :param handle: Handle of the stream to close.
        :type handle: StreamHandle
        """
        return (
            cls.build_send_payload("close", {
                "handle": handle,
            }),
            None
        )

