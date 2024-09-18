from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        users_list = [
            {"email": "user1@sky.com", "phone": "1234567890"},
            {"email": "moderator@sky.com", "phone": "0987654321", "city": "Moscow"},
            {"email": "user2@sky.com", "city": "Berlin"},
        ]

        prepare_to_fill_users_list = []
        for user_data in users_list:
            prepare_to_fill_users_list.append(User(**user_data))
        User.objects.bulk_create(prepare_to_fill_users_list)
