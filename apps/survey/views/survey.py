from rest_framework import generics

from apps.survey.models import Survey
from apps.survey.serializers.survey import SurveySerializer


class SurveyCreateAPIView(generics.CreateAPIView):
    serializer_class = SurveySerializer


class SurveyListAPIView(generics.ListAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

class SurveyDetailAPIView(generics.RetrieveAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()


class SurveyUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

class SurveyDeleteAPIView(generics.DestroyAPIView):
    queryset = Survey.objects.all()
