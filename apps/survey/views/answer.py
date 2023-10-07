from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Answer
from apps.survey.permissions import IsOwnerPermission
from apps.survey.serializers.answer import AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


class AnswerDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)
