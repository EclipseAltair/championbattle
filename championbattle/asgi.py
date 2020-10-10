# coding=utf-8
# stdlib
import os

# django
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "championbattle.settings.base")

application = get_asgi_application()
