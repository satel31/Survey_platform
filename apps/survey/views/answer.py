from rest_framework import generics

from apps.survey.models import Answer
from apps.survey.serializers.answer import AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer


class AnswerDeleteAPIView(generics.DestroyAPIView):
    queryset = Answer.objects.all()
