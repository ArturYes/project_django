import configparser
import os

from django.core.management import BaseCommand

from apps.users.models import User

# Getting data from the config.ini file
config = configparser.ConfigParser()
config.read("config.ini")


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=config['admin']['email'],
            is_staff=True,
            is_superuser=True
        )
        user.set_password(config['admin']['password'])
        user.save()
