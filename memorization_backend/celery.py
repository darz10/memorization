import os

from django.conf import settings
from celery import Celery


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'memorization_backend.settings'
)

app = Celery('memorization_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_url = settings.CELERY_BROKER_URL

app.conf.beat_schedule = {
    'notification_reminders': {
        'task': 'reminder.tasks.notification_reminders',
        'schedule': 5,
    },
}
