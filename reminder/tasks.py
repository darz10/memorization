from celery import shared_task

from reminder.enums.reminder_status import ReminderStatus
from reminder.models.reminder import Reminder
from websocket.consumers.reminder_status import reminder_notification_message


@shared_task
def notification_reminders():
    """
    Function responsible for logic send notification reminders
    """
    for status in ReminderStatus.statuses_for_repeat():
        reminders = Reminder.objects.get_reminders_for_send_repeats(
            status.value
        )
        for reminder in reminders:
            data = {"text": reminder.text, "status": reminder.status}
            reminder_notification_message(reminder.user_id, data)
        reminders.update(status=ReminderStatus.next_status(status).value)
