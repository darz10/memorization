from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from accounts.models.user import User

from reminder.enums.reminder_status import (
    ReminderStatus,
    ReminderStatusTimedelta
)


class ReminderManager(models.Manager):
    def get_reminders_for_send_repeats(self, status: str):
        """
        Get all records for send notification repeats
        """
        time_now = now()
        timedelta_status = ReminderStatusTimedelta[status].value
        min_delta, max_delta = timedelta_status
        if min_delta and max_delta:
            params = models.Q(diff_time__gte=min_delta) \
                and models.Q(diff_time__lte=max_delta)
        elif min_delta:
            params = models.Q(diff_time__gte=min_delta)
        return super().get_queryset().annotate(
            diff_time=time_now - models.F('created_at')
        ).filter(params)

    def user_own_reminders(self, user: User):
        """
        Get reminders of user
        """
        return super().get_queryset().filter(
            user=user
        ).select_related("user")


class Reminder(models.Model):
    """
    Reminder class
    """
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name="user_reminders",
        verbose_name=_("Execution status")
    )
    text = models.TextField(verbose_name=_("Text we want to remember"))
    status = models.CharField(
        max_length=50,
        choices=ReminderStatus.choices(),
        default=ReminderStatus.SECOND_REPEAT.value,
        verbose_name=_("Execution status")
    )
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ReminderManager()

    class Meta:
        verbose_name = _('Reminder')
        verbose_name_plural = _('Reminders')
