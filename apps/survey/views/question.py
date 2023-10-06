from rest_framework import generics

from apps.survey.models import Question, Answer
from apps.survey.serializers.question import QuestionSerializer, QuestionWithAnswerSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = QuestionSerializer


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_serializer_class(self):
        if Answer.objects.filter(question=self.get_object().pk, user=self.request.user.pk).exists():
            return QuestionWithAnswerSerializer
        return QuestionSerializer


class QuestionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
