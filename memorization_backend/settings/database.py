from .base import get_env_value


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_value("DBNAME", ""),
        'USER':  get_env_value('DBUSER', default='postgres'),
        'PASSWORD': get_env_value('DBPASSWORD', default='postgrespass'),
        'HOST': get_env_value("DBHOST", "localhost"),
        'PORT': get_env_value("DBPORT", 5432,)
    }
}
