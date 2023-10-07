from django.conf import settings
from django.core.mail import send_mail

from apps.user.models import User


def share_email(email_to, user, survey):
    """Отправка email с рекомендацией опроса"""
    send_mail(
        f'{user.first_name} {user.last_name} send a survey to you!',
        f'Check it out! {survey.survey_name} (http://localhost:8000/survey/surveys/{survey.pk})',
        settings.EMAIL_HOST_USER,
        [email_to]
    )


def new_survey_email(user, survey):
    """Отправка email с новым опросом"""
    user_emails = [u.email for u in User.objects.exclude(pk=user.pk)]
    send_mail(
        f'New survey!',
        f'{user.email} has a new survey! Check it out! (http://localhost:8000/survey/surveys/{survey.pk})',
        settings.EMAIL_HOST_USER,
        user_emails
    )


def new_like_email(email_to, survey):
    """Отправка email с уведомлением об оценке опроса"""
    send_mail(
        f'New like!',
        f'You have got a new like/dislike for your survey {survey.survey_name}',
        settings.EMAIL_HOST_USER,
        [email_to]
    )
