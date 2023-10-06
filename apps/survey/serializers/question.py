from rest_framework import serializers

from apps.survey.models import Question
from apps.survey.serializers.answer import AnswerSerializer
from apps.survey.serializers.choice import ChoiceSerializer


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(read_only=True, many=True)
    user_answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'
