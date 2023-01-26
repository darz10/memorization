import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

from websocket.urls import router
from websocket.middleware import CustomTokenAuthMiddleware


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'memorization_backend.settings'
)


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": CustomTokenAuthMiddleware(router),
    }
)
