# coding=utf-8
# stdlib
import os

# django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "championbattle.settings.base")

application = get_wsgi_application()
