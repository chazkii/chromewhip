# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import runtime as Runtime

# ConsoleMessage: Console message.
class ConsoleMessage(ChromeTypeBase):
    def __init__(self,
                 source: Union['str'],
                 level: Union['str'],
                 text: Union['str'],
                 url: Optional['str'] = None,
                 line: Optional['int'] = None,
                 column: Optional['int'] = None,
                 ):

        self.source = source
        self.level = level
        self.text = text
        self.url = url
        self.line = line
        self.column = column


class Console(PayloadMixin):
    """ This domain is deprecated - use Runtime or Log instead.
    """
    @classmethod
    def enable(cls):
        """Enables console domain, sends the messages collected so far to the client by means of the <code>messageAdded</code> notification.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables console domain, prevents further console messages from being reported to the client.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def clearMessages(cls):
        """Does nothing.
        """
        return (
            cls.build_send_payload("clearMessages", {
            }),
            None
        )



class MessageAddedEvent(BaseEvent):

    js_name = 'Console.messageAdded'
    hashable = []
    is_hashable = False

    def __init__(self,
                 message: Union['ConsoleMessage', dict],
                 ):
        if isinstance(message, dict):
            message = ConsoleMessage(**message)
        self.message = message

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
