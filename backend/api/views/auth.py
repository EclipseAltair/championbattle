# coding=utf-8
# django
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# app
from ..serializers.auth import UserSerializer


class UserCreateView(CreateAPIView):
    """ Создание пользователя """

    serializer_class = UserSerializer


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    """ Получение, обновление данных пользователя """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get("user", {})

        serializer = UserSerializer(request.user, data=serializer_data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
