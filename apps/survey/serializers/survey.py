from rest_framework import serializers

from apps.survey.models import Survey, Question, Like
from apps.survey.serializers.question import QuestionSerializer


class SurveySerializer(serializers.ModelSerializer):
    """Сериализатор для опроса (с количеством вопросов и вопросами)"""
    question_count = serializers.SerializerMethodField()
    questions = QuestionSerializer(read_only=True, many=True)
    likes = serializers.SerializerMethodField()

    def get_question_count(self, survey):
        return Question.objects.filter(survey=survey.pk).count()

    def get_likes(self, survey):
        return Like.objects.filter(survey=survey.pk, like=True).count()

    class Meta:
        model = Survey
        fields = '__all__'
