# coding=utf-8
# django
from django.urls import path

# project
from backend.api.views.auth import SignUpView

app_name = "api"
urlpatterns = [
    path("signup/", SignUpView.as_view()),
]
