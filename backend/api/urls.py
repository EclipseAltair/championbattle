# coding=utf-8
# thirdparty
from rest_framework_jwt.views import obtain_jwt_token

# django
from django.urls import path

# project
from backend.api.views.auth import UserCreateView, UserRetrieveUpdateView

app_name = "api"
urlpatterns = [
    path("auth/create/", UserCreateView.as_view()),
    path("auth/obtain_token/", obtain_jwt_token),
    path("auth/update/", UserRetrieveUpdateView.as_view()),
]
