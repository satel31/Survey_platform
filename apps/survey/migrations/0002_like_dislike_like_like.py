# Generated by Django 4.2.5 on 2023-10-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='dislike',
            field=models.BooleanField(default=False, verbose_name='Dislike'),
        ),
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=False, verbose_name='Like'),
        ),
    ]
