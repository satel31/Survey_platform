from rest_framework import serializers

from apps.survey.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """Сериализатор для оценки опроса пользователем"""

    class Meta:
        model = Like
        fields = '__all__'
