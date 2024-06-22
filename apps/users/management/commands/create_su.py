import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.users.models import User
from config.settings import BASE_DIR

# Getting data from the .env file
dotenv_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('admin_email'),
            is_staff=True,
            is_superuser=True
        )
        user.set_password(os.getenv('admin_password'))
        user.save()
