from rest_framework import generics

from apps.survey.models import Like
from apps.survey.serializers.like import LikeSerializer


class LikeCreateAPIView(generics.CreateAPIView):
    serializer_class = LikeSerializer


class LikeListAPIView(generics.ListAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class LikeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class LikeDeleteAPIView(generics.DestroyAPIView):
    queryset = Like.objects.all()
