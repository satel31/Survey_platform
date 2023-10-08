from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.survey.models import Survey
from apps.survey.permissions import IsOwnerPermission
from apps.survey.serializers.survey import SurveySerializer
from apps.survey.services import share_email, new_survey_email


class SurveyCreateAPIView(generics.CreateAPIView):
    """Создание опроса.
       Для создания отпроса необходимо ввести имя опроса.
       Доступно только для авторизованного пользователя."""
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_survey = serializer.save()
        new_survey.user = self.request.user
        new_survey_email(self.request.user, new_survey)
        new_survey.save()


class SurveyListAPIView(generics.ListAPIView):
    """Получение списка опросов.
       Есть фильтр и поиск по имени опроса и пользователю-создателю.
       Доступно только для авторизованных пользователей."""
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['survey_name', 'user',]
    filterset_fields = ('survey_name', 'user',)


class SurveyDetailAPIView(generics.RetrieveAPIView):
    """Получение конкретного опроса по его pk.
       Доступно только для авторизованных пользователей."""
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated]


class SurveyUpdateAPIView(generics.UpdateAPIView):
    """Обновление опроса.
       Доступно только для владельца опроса."""
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]


class SurveyDeleteAPIView(generics.DestroyAPIView):
    """Удаление опроса.
       Доступно только для владельца вопроса."""
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]


class SurveyShare(APIView):
    """Отправка пользователю указанного опроса.
       Чтобы поделиться опросом необходимо ввести email получателя и pk опроса.
       Не возвращает никакие данные.
    """
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    serializer_class = SurveySerializer

    def post(self, request, *args, **kwargs):
        email_to = request.data['email']
        survey_pk = request.data['survey']
        survey = Survey.objects.get(pk=survey_pk)
        share_email(email_to, request.user, survey)
