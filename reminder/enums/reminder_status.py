from datetime import timedelta

from .base_enum import BaseEnum


class ReminderStatus(BaseEnum):
    SECOND_REPEAT = "SECOND_REPEAT"
    THIRD_REPEAT = "THIRD_REPEAT"
    FOURTH_REPEAT = "FOURTH_REPEAT"
    DONE = "DONE"

    @classmethod
    def next_status(cls, current_status):
        """
        Function return next status,
        if next status doesn't exists return current status
        """
        statuses = list(cls)
        for idx in range(len(statuses)):
            if statuses[idx] == current_status:
                if idx + 1 < len(statuses):
                    return statuses[idx + 1]
                else:
                    return current_status

    @classmethod
    def statuses_for_repeat(cls):
        """
        Get list statuses for send notification
        """
        return [
            cls.FOURTH_REPEAT,
            cls.THIRD_REPEAT,
            cls.SECOND_REPEAT,
        ]


class ReminderStatusTimedelta(BaseEnum):
    SECOND_REPEAT = (timedelta(minutes=20), timedelta(days=1))
    THIRD_REPEAT = (timedelta(days=1), timedelta(weeks=1))
    FOURTH_REPEAT = (timedelta(weeks=1), None)
