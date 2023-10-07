from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Survey
from apps.survey.permissions import IsOwnerPermission
from apps.survey.serializers.survey import SurveySerializer


class SurveyCreateAPIView(generics.CreateAPIView):
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_survey = serializer.save()
        new_survey.user = self.request.user
        new_survey.save()


class SurveyListAPIView(generics.ListAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['survey_name', 'user']
    filterset_fields = ('survey_name', 'user',)

class SurveyDetailAPIView(generics.RetrieveAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated]


class SurveyUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]

class SurveyDeleteAPIView(generics.DestroyAPIView):
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission]
