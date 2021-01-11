from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.filter(username='admin1'):
            print('Admin user already exists')
        else:
            User.objects.create_superuser(
                username='admin1',
                password='admin',
            )
            
            print('Admin user created')

