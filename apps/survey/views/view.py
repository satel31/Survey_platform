from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import View
from apps.survey.permissions import IsSurveyOwnerPermission
from apps.survey.serializers.view import ViewSerializer


class ViewCreateAPIView(generics.CreateAPIView):
    """Создание просмотра.
       Для создания просмотра необходимо ввести pk опроса.
       Доступно только для авторизованного пользователя."""
    serializer_class = ViewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_view = serializer.save()
        new_view.user = self.request.user
        new_view.save()


class ViewListAPIView(generics.ListAPIView):
    """Получение списка просмотров пользователя.
       Доступно только для авторизованных пользователей."""
    serializer_class = ViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return View.objects.filter(user=self.request.user)


class ViewDeleteAPIView(generics.DestroyAPIView):
    """Удаление просмотра.
       Доступно только для владельца просмотра."""
    queryset = View.objects.all()
    permission_classes = [IsAuthenticated, IsSurveyOwnerPermission]
