# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# PressureLevel: Memory pressure level.
PressureLevel = str

class Memory(PayloadMixin):
    """ 
    """
    @classmethod
    def getDOMCounters(cls):
        """
        """
        return (
            cls.build_send_payload("getDOMCounters", {
            }),
            cls.convert_payload({
                "documents": {
                    "class": int,
                    "optional": False
                },
                "nodes": {
                    "class": int,
                    "optional": False
                },
                "jsEventListeners": {
                    "class": int,
                    "optional": False
                },
            })
        )

    @classmethod
    def setPressureNotificationsSuppressed(cls,
                                           suppressed: Union['bool'],
                                           ):
        """Enable/disable suppressing memory pressure notifications in all processes.
        :param suppressed: If true, memory pressure notifications will be suppressed.
        :type suppressed: bool
        """
        return (
            cls.build_send_payload("setPressureNotificationsSuppressed", {
                "suppressed": suppressed,
            }),
            None
        )

    @classmethod
    def simulatePressureNotification(cls,
                                     level: Union['PressureLevel'],
                                     ):
        """Simulate a memory pressure notification in all processes.
        :param level: Memory pressure level of the notification.
        :type level: PressureLevel
        """
        return (
            cls.build_send_payload("simulatePressureNotification", {
                "level": level,
            }),
            None
        )

