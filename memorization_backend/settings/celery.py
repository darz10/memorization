from .base import REDIS_DOMAIN


CELERY_BROKER_URL = f'redis://{REDIS_DOMAIN}/0'

CELERY_RESULT_BACKEND = CELERY_BROKER_URL
