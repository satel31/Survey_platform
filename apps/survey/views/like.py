from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.survey.models import Like
from apps.survey.permissions import IsOwnerPermission
from apps.survey.serializers.like import LikeSerializer
from apps.survey.services import new_like_email


class LikeCreateAPIView(generics.CreateAPIView):
    """Создание лайка/дизлайка для опроса.
       Для создания ответа необходимо ввести pk опроса и True для лайка/дизлайка.
       Доступно только для авторизованного пользователя."""
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_like = serializer.save()
        new_like.user = self.request.user
        new_like_email(new_like.survey.user.email, new_like.survey)
        new_like.save()


class LikeListAPIView(generics.ListAPIView):
    """Получение списка всех оценок пользователяопросам.
       Доступно только для авторизованных пользователей."""
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)


class LikeUpdateAPIView(generics.UpdateAPIView):
    """Обновление оценки.
       Доступно только для авторизованных пользователей."""
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    queryset = Like.objects.all()


class LikeDeleteAPIView(generics.DestroyAPIView):
    """Удаление лайка/дизлайка.
       Доступно только для владельца оценки."""
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    queryset = Like.objects.all()
