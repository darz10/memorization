from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import jwt


User = get_user_model()


@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


class CustomTokenAuthMiddlewareInstance:
    """
    Middleware for auth by token in Django Channels
    """

    def __init__(self, scope, middleware):
        self.middleware = middleware
        self.scope = dict(scope)
        self.inner = self.middleware.inner

    async def __call__(self, receive, send):
        scope = self.scope
        headers = scope['headers']
        headers_as_dict = dict(headers)
        token_b = headers_as_dict.get(b'authorization')
        if token_b:
            token_key = token_b.decode('utf-8')
            try:
                token_name, token = token_key.split()
                if token_name == "Bearer":
                    user_jwt = JSONWebTokenAuthentication.jwt_decode_token(
                        token
                    )
                    user = await get_user(user_jwt['user_id'])
                    scope['user'] = user
            except (jwt.InvalidSignatureError, ValueError):
                scope['user'] = AnonymousUser()
        return await self.inner(scope, receive, send)


class CustomTokenAuthMiddleware:
    """
    Custom auth user by token
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return CustomTokenAuthMiddlewareInstance(scope, self)
