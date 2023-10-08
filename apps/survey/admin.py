from django.contrib import admin

from apps.survey.models import Survey, Question, Choice, Answer, View, Like


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('survey_name', 'user', 'description',)
    list_filter = ('survey_name', 'user',)
    search_fields = ('survey_name', 'description',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'text',)
    list_filter = ('survey',)
    search_fields = ('survey', 'text',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'text',)
    list_filter = ('question',)
    search_fields = ('question', 'text',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'choice',)
    list_filter = ('user', 'question', 'choice',)


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'survey',)
    list_filter = ('user', 'survey',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'survey', 'like', 'dislike',)
    list_filter = ('user', 'survey', 'like', 'dislike',)
