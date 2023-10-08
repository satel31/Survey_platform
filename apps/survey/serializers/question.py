from rest_framework import serializers

from apps.survey.models import Question
from apps.survey.serializers.answer import AnswerSerializer
from apps.survey.serializers.choice import ChoiceSerializer


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопроса (с вариантами ответа)"""
    choices = ChoiceSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    """Сериализатор для вопроса (с вариантами ответа и ответом пользователя)"""
    choices = ChoiceSerializer(read_only=True, many=True)
    user_answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'
