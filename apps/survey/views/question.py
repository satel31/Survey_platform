from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Question, Answer
from apps.survey.permissions import IsSurveyOwnerPermission
from apps.survey.serializers.question import QuestionSerializer, QuestionWithAnswerSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    """Создание вопроса для опроса.
       Для создания ответа необходимо ввести pk опроса и текст вопроса.
       Доступно только для авторизованного пользователя."""
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class QuestionListAPIView(generics.ListAPIView):
    """Получение списка вопросов.
       Есть фильтр и поиск по опросу и тексту вопроса.
       Доступно только для авторизованных пользователей."""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['survey']
    filterset_fields = ('text',)


class QuestionDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного вопроса по его pk.
       При наличии у пользователя ответа на вопрос будет выведен также его ответ.
       Доступно только для авторизованных пользователей."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if Answer.objects.filter(question=self.get_object().pk, user=self.request.user.pk).exists():
            return QuestionWithAnswerSerializer
        return QuestionSerializer


class QuestionUpdateAPIView(generics.UpdateAPIView):
    """Обновление вопроса.
       Доступно только для владельца ответа."""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsSurveyOwnerPermission]


class QuestionDeleteAPIView(generics.DestroyAPIView):
    """Удаление вопроса.
       Доступно только для владельца вопроса."""
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, IsSurveyOwnerPermission]
