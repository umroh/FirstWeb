"""
WSGI config for prototypeAsisten project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prototypeAsisten.settings")

application = get_wsgi_application()

path = '/templates/home.html'  # use your own username here
if path not in sys.path:
    sys.path.append(path)
