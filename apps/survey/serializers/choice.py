from rest_framework import serializers

from apps.survey.models import Choice


class ChoiceSerializer(serializers.ModelSerializer):
    """Сериализатор для варианта ответа"""

    class Meta:
        model = Choice
        fields = '__all__'
