from rest_framework import generics

from apps.survey.models import Choice
from apps.survey.serializers.choice import ChoiceSerializer


class ChoiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ChoiceSerializer

class ChoiceDeleteAPIView(generics.DestroyAPIView):
    queryset = Choice.objects.all()
