# coding=utf-8
# django
from rest_framework.response import Response
from rest_framework.views import APIView


class SwaggerAPIView(APIView):
    """ Документация API """

    def get(self, request, *args, **kwargs):
        return Response("qwe")
