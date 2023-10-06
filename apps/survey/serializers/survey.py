from rest_framework import serializers

from apps.survey.models import Survey, Question
from apps.survey.serializers.question import QuestionSerializer


class SurveySerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField()
    questions = QuestionSerializer(read_only=True, many=True)

    def get_question_count(self, survey):
        return Question.objects.filter(survey=survey.pk).count()

    class Meta:
        model = Survey
        fields = '__all__'
