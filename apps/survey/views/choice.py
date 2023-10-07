from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Choice
from apps.survey.permissions import IsChoiceOwnerPermission
from apps.survey.serializers.choice import ChoiceSerializer


class ChoiceCreateAPIView(generics.CreateAPIView):
    """Создание варианта ответа на вопрос.
       Для создания ответа необходимо ввести pk опроса и вариант ответа.
       Доступно только для авторизованного пользователя."""
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated]

class ChoiceDeleteAPIView(generics.DestroyAPIView):
    """Удаление варианта ответа на вопрос.
       Доступно только для владельца варианта ответа."""
    queryset = Choice.objects.all()
    permission_classes = [IsAuthenticated, IsChoiceOwnerPermission]

