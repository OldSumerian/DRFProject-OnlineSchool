from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        users_list = [
            {"email": "user1@sky.pro", "phone": "1234567890", 'password': make_password('123')},
            {"email": "moderator@sky.pro", "phone": "0987654321", "city": "Moscow", 'password': make_password('234')},
            {"email": "user2@sky.pro", "city": "Berlin", 'password': make_password('345')},
        ]

        prepare_to_fill_users_list = []
        for user_data in users_list:
            prepare_to_fill_users_list.append(User(**user_data))
        User.objects.bulk_create(prepare_to_fill_users_list)
