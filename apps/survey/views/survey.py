from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Survey
from apps.survey.permissions import IsOwnerPermission
from apps.survey.serializers.survey import SurveySerializer


class SurveyCreateAPIView(generics.CreateAPIView):
    serializer_class = SurveySerializer
    permission_classes = [IsAuthenticated]


class SurveyListAPIView(generics.ListAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    permission_classes = [IsAuthenticated]

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
