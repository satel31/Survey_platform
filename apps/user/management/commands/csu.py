from django.core.management import BaseCommand

from apps.user.models import User


class Command(BaseCommand):
    """Created superuser"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@test.ru',
            first_name='Admin',
            last_name='test',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('123456')
        user.save()
