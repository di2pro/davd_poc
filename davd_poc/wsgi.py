"""
WSGI config for davd_poc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings = os.getenv('SETTINGS', 'base')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"davd_poc.settings.{settings}")

application = get_wsgi_application()
