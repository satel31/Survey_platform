# Generated by Django 4.2.5 on 2023-10-07 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_answer_question_alter_choice_question_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='owner',
            new_name='user',
        ),
    ]
