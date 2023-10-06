from rest_framework import generics

from apps.survey.models import View
from apps.survey.serializers.view import ViewSerializer


class ViewCreateAPIView(generics.CreateAPIView):
    serializer_class = ViewSerializer


class ViewListAPIView(generics.ListAPIView):
    serializer_class = ViewSerializer
    queryset = View.objects.all()


class ViewUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ViewSerializer
    queryset = View.objects.all()


class ViewDeleteAPIView(generics.DestroyAPIView):
    queryset = View.objects.all()
