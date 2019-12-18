"""
WSGI config for initial_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings = os.getenv('SETTINGS', 'base')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"initial_project.settings.{settings}")

application = get_wsgi_application()
