from django.urls import re_path

from channels.routing import URLRouter

from . import consumers


router = URLRouter([
    re_path(r'ws/notifications/$', consumers.ReminderStatusConsumer.as_asgi()),
])
