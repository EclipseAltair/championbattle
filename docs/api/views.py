# coding=utf-8
# stdlib
import json

# thirdparty
import yaml

# django
from django.shortcuts import render


def swagger_api_view(request):
    """ Документация API """

    with open("backend/api/api.yml") as f:
        data = yaml.load(f.read(), Loader=yaml.Loader)
        data = json.dumps(data)
    return render(request, "docs/api/swagger.html", {"data": data})
