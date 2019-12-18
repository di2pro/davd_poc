from .base import *  # noqa

SECRET_KEY = 'secret_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'initial_project',
        'USER': 'initial_project',
        'PASSWORD': 'initial_project',
        'HOST': 'localhost',
        'PORT': 5433,
    }
}
