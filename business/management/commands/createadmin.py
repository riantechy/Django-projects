from django.core.management.base import BaseCommand
from accounts.models import Account


class Command(BaseCommand):
    help = 'Creates a superuser account with static values'

    def handle(self, *args, **options):
        email = 'me@gmail.com'
        username = 'me'
        password = 'me'
        confirm_password = 'me'
        phone_number = '07905311065'

        if password != confirm_password:
            self.stdout.write(self.style.ERROR('Password and Confirm Password do not match'))
            return

        try:
            user = Account.objects.create_user(email=email, username=username, password=password, phone_number=phone_number)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
