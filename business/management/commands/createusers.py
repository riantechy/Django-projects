from django.core.management.base import BaseCommand
from accounts.models import Account
from django.contrib.auth.hashers import make_password
from faker import Faker

class Command(BaseCommand):
    help = 'Creates a specified number of superuser accounts with random values'

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help='Number of superuser accounts to create')

    def handle(self, *args, **options):
        fake = Faker()
        num_users = options['num_users']

        for i in range(num_users):
            email = fake.email()
            username = fake.user_name()
            password = fake.password()
            phone_number = fake.phone_number()
            country_code = fake.country_code()
            Account.objects.create_user(email=email, username=username, password=password,
                                         phone_number=phone_number, country_code=country_code,
                                         is_staff=True, is_superuser= False)

        self.stdout.write(self.style.SUCCESS(f'{num_users} user accounts created successfully.'))
