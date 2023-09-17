import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from profiles.models import Profile
from business.models import Business


class Command(BaseCommand):
    help = "Create fake businesses"

    def add_arguments(self, parser):
        parser.add_argument('num_businesses', type=int, help='Number of businesses to create')

    def handle(self, *args, **options):
        fake = Faker()
        num_businesses = options['num_businesses']
        profiles = Profile.objects.all()

        for i in range(num_businesses):
            # Generate fake data
            name = fake.company()
            address = fake.address()
            phone_number = fake.phone_number()
            email = fake.email()
            website = fake.url()
            description = fake.text(max_nb_chars=200)
            industry = fake.job()
            founded_in = fake.date_this_century(before_today=True, after_today=False)
            employee_count = random.randint(1, 100)
            id_number = fake.random_number(digits=13)
            kra_pin = fake.random_number(digits=10)
            bs_reg_number = fake.random_number(digits=10)
            bs_permit_number = fake.random_number(digits=10)
            id_attachment = fake.file_name(extension="pdf")
            business_permit = fake.file_name(extension="pdf")
            kra_pin_attachment = fake.file_name(extension="pdf")
            social_media_links = {
                "twitter": fake.url(),
                "facebook": fake.url(),
                "linkedin": fake.url(),
            }
            owner = profiles[random.randint(0, len(profiles) - 1)] if len(profiles) > 0 else None

            # Create a new Business object with the fake data and save it
            business = Business.objects.create(
                name=name,
                address=address,
                phone_number=phone_number,
                email=email,
                website=website,
                description=description,
                industry=industry,
                founded_in=founded_in,
                employee_count=employee_count,
                id_number=id_number,
                kra_pin=kra_pin,
                bs_reg_number=bs_reg_number,
                bs_permit_number=bs_permit_number,
                id_attachment=id_attachment,
                business_permit=business_permit,
                kra_pin_attachment=kra_pin_attachment,
                social_media_links=social_media_links,
                owner=owner,
                is_verified=True,  # optional: set the initial state of the is_verified field
                is_top_rated=False,  # optional: set the initial state of the is_top_rated field
            )

            self.stdout.write(f"Created business: {business.name}")
        self.stdout.write(self.style.SUCCESS(f'{num_businesses} businesses created successfully.'))
