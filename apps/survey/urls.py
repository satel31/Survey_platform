from django.urls import path

from apps.survey.views.answer import AnswerCreateAPIView, AnswerDeleteAPIView
from apps.survey.views.choice import ChoiceCreateAPIView, ChoiceDeleteAPIView
from apps.survey.views.like import LikeCreateAPIView, LikeListAPIView, LikeUpdateAPIView, LikeDeleteAPIView
from apps.survey.views.question import QuestionCreateAPIView, QuestionListAPIView, QuestionDetailAPIView, \
    QuestionUpdateAPIView, QuestionDeleteAPIView
from apps.survey.views.survey import SurveyCreateAPIView, SurveyListAPIView, SurveyDetailAPIView, SurveyUpdateAPIView, \
    SurveyDeleteAPIView, SurveyShare
from apps.survey.views.view import ViewCreateAPIView, ViewListAPIView, ViewDeleteAPIView

app_name = 'survey'

urlpatterns = [
    # survey
    path('add_survey/', SurveyCreateAPIView.as_view(), name='add_survey'),
    path('surveys/', SurveyListAPIView.as_view(), name='surveys'),
    path('surveys/<int:pk>/', SurveyDetailAPIView.as_view(), name='survey'),
    path('surveys/update/<int:pk>/', SurveyUpdateAPIView.as_view(), name='survey_update'),
    path('surveys/delete/<int:pk>/', SurveyDeleteAPIView.as_view(), name='survey_delete'),

    # question
    path('add_question/', QuestionCreateAPIView.as_view(), name='add_question'),
    path('questions/', QuestionListAPIView.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question'),
    path('questions/update/<int:pk>/', QuestionUpdateAPIView.as_view(), name='question_update'),
    path('questions/delete/<int:pk>/', QuestionDeleteAPIView.as_view(), name='question_delete'),

    # choice
    path('add_choice/', ChoiceCreateAPIView.as_view(), name='add_choice'),
    path('choice/delete/<int:pk>/', ChoiceDeleteAPIView.as_view(), name='choice_delete'),

    # answer
    path('add_answer/', AnswerCreateAPIView.as_view(), name='add_answer'),
    path('answer/delete/<int:pk>/', AnswerDeleteAPIView.as_view(), name='answer_delete'),

    # view
    path('add_view/', ViewCreateAPIView.as_view(), name='add_view'),
    path('views/', ViewListAPIView.as_view(), name='views'),
    path('views/delete/<int:pk>/', ViewDeleteAPIView.as_view(), name='view_delete'),

    # like
    path('add_like/', LikeCreateAPIView.as_view(), name='add_view'),
    path('likes/', LikeListAPIView.as_view(), name='views'),
    path('likes/update/<int:pk>/', LikeUpdateAPIView.as_view(), name='view_update'),
    path('likes/delete/<int:pk>/', LikeDeleteAPIView.as_view(), name='view_delete'),

    # share
    path('share/', SurveyShare.as_view(), name='share'),
]
