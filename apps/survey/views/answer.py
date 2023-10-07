from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Answer
from apps.survey.permissions import IsOwnerPermission
from apps.survey.serializers.answer import AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_answer = serializer.save()
        new_answer.user = self.request.user
        new_answer.save()



class AnswerDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    queryset = Answer.objects.all()
