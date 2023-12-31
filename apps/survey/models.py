from django.db import models

from apps.user.models import User

NULLABLE = {'blank': True, 'null': True}


class Survey(models.Model):
    """Модель опроса"""
    survey_name = models.CharField(max_length=235, verbose_name='Survey name', unique=True)
    description = models.TextField(max_length=4_096, verbose_name='Survey description', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE, related_name='surveys')

    def __str__(self):
        return f'{self.survey_name} by {self.user}'

    class Meta:
        verbose_name = 'survey'
        verbose_name_plural = 'surveys'


class Question(models.Model):
    """Модель вопроса"""
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Survey', related_name='questions')
    text = models.CharField(max_length=4_096, verbose_name='Text of the question')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Choice(models.Model):
    """Модель варианта ответа"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question', related_name='choices')
    text = models.CharField(max_length=4_096, verbose_name='Text of the choice')

    def __str__(self):
        return f'{self.text}'


class Answer(models.Model):
    """Модель ответа пользователя"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question',
                                 related_name='user_answers')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name='User choice')
    text = models.CharField(max_length=4_096, verbose_name='Text of the answer', **NULLABLE)

    def __str__(self):
        return f'User answer to question {self.question}'

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'


class View(models.Model):
    """Модель просмотра опроса"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE, related_name='views')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Survey')

    def __str__(self):
        return f'Views of {self.user}, survey: {self.survey}'

    class Meta:
        verbose_name = 'view'
        verbose_name_plural = 'views'


class Like(models.Model):
    """Модель оценки опроса (лайк/дизлайк)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', **NULLABLE,
                             related_name='assessments')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Survey')
    like = models.BooleanField(default=False, verbose_name='Like')
    dislike = models.BooleanField(default=False, verbose_name='Dislike')

    def __str__(self):
        return f'Like of {self.user}, survey: {self.survey}'

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'
