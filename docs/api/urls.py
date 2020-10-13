# coding=utf-8
# django
from django.conf.urls import url

# app
from .views import swagger_api_view

app_name = "api_docs"
urlpatterns = [
    url(r"^$", swagger_api_view, name="swagger_api"),
]
