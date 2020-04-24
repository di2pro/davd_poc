from .base import *  # noqa

SECRET_KEY = 'secret_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'davd_poc',
        'USER': 'davd_poc',
        'PASSWORD': 'davd_poc',
        'HOST': 'localhost',
        'PORT': 5433,
    }
}
