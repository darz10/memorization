from reminder.models import Reminder
from reminder.enums.reminder_status import ReminderStatus


def set_reminder_third_repeat_status(reminder: Reminder) -> None:
    """
    Change reminder status to third_repeat
    """
    reminder.status = ReminderStatus.THIRD_REPEAT.value
    reminder.save()


def set_reminder_fourth_repeat_status(reminder: Reminder) -> None:
    """
    Change reminder status to fourth_repeat
    """
    reminder.status = ReminderStatus.FOURTH_REPEAT.value
    reminder.save()


def set_reminder_done_status(reminder: Reminder) -> None:
    """
    Change reminder status to done
    """
    reminder.status = ReminderStatus.DONE.value
    reminder.save()
