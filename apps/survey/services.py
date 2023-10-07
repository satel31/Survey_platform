from django.conf import settings
from django.core.mail import send_mail

from apps.user.models import User


def share_email(email_to, user, survey):
    send_mail(
        f'{user.first_name} {user.last_name} send a survey to you!',
        f'Check it out! {survey.survey_name} (http://localhost:8000/survey/surveys/{survey.pk})',
        settings.EMAIL_HOST_USER,
        [email_to]
    )


def new_survey_email(user, survey):
    user_emails = [u.email for u in User.objects.exclude(pk=user.pk)]
    send_mail(
        f'New survey!',
        f'{user.email} has a new survey! Check it out! (http://localhost:8000/survey/surveys/{survey.pk})',
        settings.EMAIL_HOST_USER,
        user_emails
    )


def new_like_email(email_to, survey):
    send_mail(
        f'New like!',
        f'You have got a new like for your survey {survey.survey_name}',
        settings.EMAIL_HOST_USER,
        [email_to]
    )
