from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Choice
from apps.survey.permissions import IsChoiceOwnerPermission
from apps.survey.serializers.choice import ChoiceSerializer


class ChoiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated]

class ChoiceDeleteAPIView(generics.DestroyAPIView):
    queryset = Choice.objects.all()
    permission_classes = [IsAuthenticated, IsChoiceOwnerPermission]

