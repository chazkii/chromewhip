# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

class Inspector(PayloadMixin):
    """ 
    """
    @classmethod
    def enable(cls):
        """Enables inspector domain notifications.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables inspector domain notifications.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )



class DetachedEvent(BaseEvent):

    js_name = 'Inspector.detached'
    hashable = []
    is_hashable = False

    def __init__(self,
                 reason: Union['str', dict],
                 ):
        if isinstance(reason, dict):
            reason = str(**reason)
        self.reason = reason

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class TargetCrashedEvent(BaseEvent):

    js_name = 'Inspector.targetCrashed'
    hashable = []
    is_hashable = False

    def __init__(self):
        pass

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
