from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Answer
from apps.survey.permissions import IsOwnerPermission
from apps.survey.serializers.answer import AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    """Создание ответа пользователя на вопрос опроса.
       Для создания ответа необходимо ввести pk вопроса и pk варианта ответа.
       Доступно только для авторизованного пользователя."""
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_answer = serializer.save()
        new_answer.user = self.request.user
        new_answer.save()


class AnswerDeleteAPIView(generics.DestroyAPIView):
    """Удаление ответа пользователя на вопрос опроса.
       Доступно только для владельца ответа."""
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    queryset = Answer.objects.all()
