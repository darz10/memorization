import os
from pathlib import Path

import environ


env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

env_file = os.path.join(os.path.dirname(BASE_DIR), '.env')
environ.Env.read_env(env_file=env_file)


def get_env_value(name: str, default: any = None):
    '''
    For local envs we using django-environ,
    for gitlab ci cd - private environment variabled added in repo
    '''
    return env(name, default=None) or os.environ.get(name) or default


SECRET_KEY = get_env_value('SECRET_KEY', "")

DEBUG = get_env_value("DEBUG", False)

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'rest_framework_jwt',
    'channels',
    'accounts',
    'reminder',
    'websocket',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'memorization_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'memorization_backend.wsgi.application'
ASGI_APPLICATION = 'memorization_backend.asgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend']

AUTH_USER_MODEL = 'accounts.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

base_filedir = os.path.join(os.sep, 'srv', 'memorization_files')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(base_filedir, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(base_filedir, 'media')

REDIS_SERVER = get_env_value('REDIS_SERVER', default='127.0.0.1')
REDIS_PORT = get_env_value('REDIS_PORT', default='6379')

REDIS_DOMAIN = f'{REDIS_SERVER}:{REDIS_PORT}'
