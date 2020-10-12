# coding=utf-8
# django
from django.conf.urls import url

# app
from .views import SwaggerAPIView

app_name = "api_docs"
urlpatterns = [
    url(r"^$", SwaggerAPIView.as_view(), name="swagger_api"),
]
