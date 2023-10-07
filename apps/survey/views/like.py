from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Like
from apps.survey.permissions import IsOwnerPermission
from apps.survey.serializers.like import LikeSerializer


class LikeCreateAPIView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class LikeListAPIView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)


class LikeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)


class LikeDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)
