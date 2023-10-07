from rest_framework import serializers

from apps.survey.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Сериализатор для ответа пользователя"""

    class Meta:
        model = Answer
        fields = '__all__'
