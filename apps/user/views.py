from rest_framework import generics

from apps.user.models import User
from apps.user.serializers import UserSerializer, StrangerUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = StrangerUserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.email == self.get_object().email:
            return UserSerializer
        return StrangerUserSerializer

class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
