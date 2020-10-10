# coding=utf-8
# django
from rest_framework.response import Response
from rest_framework.views import APIView


class SignUpView(APIView):
    """ Регистрация нового пользователя """

    def get(self, request):

        return Response("qwe")
