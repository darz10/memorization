from .base import REDIS_SERVER, REDIS_PORT


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(REDIS_SERVER, REDIS_PORT)],
        },
    },
}