from django.core.management.base import BaseCommand
from faker import Faker
from appliances.models import Appliance_Category, Appliance_Sub_Category, Appliance_Type, Appliance_Color, Appliance_Size, Appliance_Material, Appliance_Condition, Appliance_Brand, Appliance
from business.models import Business
import random


class Command(BaseCommand):
    help = 'Generate appliances using Faker'

    def add_arguments(self, parser):
        parser.add_argument('--categories', type=int, help='Number of appliance categories to generate')
        parser.add_argument('--sub-categories', type=int, help='Number of appliance sub-categories to generate')
        parser.add_argument('--appliances', type=int, help='Number of appliances to generate')
        parser.add_argument('--brands', type=int, help='Number of brands to generate')
        parser.add_argument('--colors', type=int, help='Number of colors to generate')
        parser.add_argument('--materials', type=int, help='Number of materials to generate')
        parser.add_argument('--conditions', type=int, help='Number of conditions to generate')

    def handle(self, *args, **options):
        fake = Faker()

        # Prompt for number of categories
        num_categories = options.get('categories')
        while not num_categories:
            try:
                num_categories = int(input('How many appliance categories do you want to generate? '))
            except ValueError:
                self.stderr.write('Invalid input. Please enter an integer.')

        # Prompt for number of sub-categories
        num_sub_categories = options.get('sub-categories')
        while not num_sub_categories:
            try:
                num_sub_categories = int(input('How many appliance sub-categories do you want to generate? '))
            except ValueError:
                self.stderr.write('Invalid input. Please enter an integer.')

        # Prompt for number of appliances
        num_appliances = options.get('appliances')
        while not num_appliances:
            try:
                num_appliances = int(input('How many appliances do you want to generate? '))
            except ValueError:
                self.stderr.write('Invalid input. Please enter an integer.')
        

        # Generate appliance categories
        categories = []
        for i in range(num_categories):
            category = Appliance_Category.objects.create(
                name=fake.word()
            )
            categories.append(category)

        # Generate appliance sub-categories
        sub_categories = []
        for i in range(num_sub_categories):
            sub_category = Appliance_Sub_Category.objects.create(
                name=fake.word(),
                category=categories[fake.random_int(min=0, max=len(categories)-1)]
            )
            sub_categories.append(sub_category)

        # Generate appliance types
        types = []
        for i in range(num_categories):
            appliance_type = Appliance_Type.objects.create(
                name=fake.word(),
                subcategory=sub_categories[fake.random_int(min=0, max=len(sub_categories)-1)]
            )
            types.append(appliance_type)

        # Generate appliance colors
        colors = []
        for i in range(num_categories):
            color = Appliance_Color.objects.create(
                name=fake.color_name()
            )
            colors.append(color)

        # Generate appliance sizes
        sizes = []
        for i in range(num_categories):
            size = Appliance_Size.objects.create(
                name=fake.random_int(min=10, max=50)
            )
            sizes.append(size)

        # Generate appliance materials
        materials = []
        for i in range(num_categories):
            material = Appliance_Material.objects.create(
                name=fake.word()
            )
            materials.append(material)

        

       # Generate appliance brands
        brands = []
        for i in range(num_categories):
            brand = Appliance_Brand.objects.create(
                name=fake.company(),
                icon=fake.image_url(width=100, height=100)
            )
            brands.append(brand)

        # Generate appliance conditions
        conditions = []
        for i in range(num_categories):
            condition = Appliance_Condition.objects.create(
                name=fake.word(),
                description=fake.text()
            )
            conditions.append(condition)

        # Generate appliances
        num_created = 0
        for i in range(num_appliances):
            owner_id = fake.random_int(min=1, max=1)
            owner = Business.objects.get(pk=owner_id)
            appliance = Appliance.objects.create(
                title=fake.word(),
                power_rating=fake.random_int(min=100, max=1000),
                category=categories[fake.random_int(min=0, max=len(categories)-1)],
                subcategory=sub_categories[fake.random_int(min=0, max=len(sub_categories)-1)],
                type=types[fake.random_int(min=0, max=len(types)-1)],
                color=colors[fake.random_int(min=0, max=len(colors)-1)],
                size=sizes[fake.random_int(min=0, max=len(sizes)-1)],
                brand=brands[fake.random_int(min=0, max=len(brands)-1)],
                material=materials[fake.random_int(min=0, max=len(materials)-1)],
                condition=conditions[fake.random_int(min=0, max=len(conditions)-1)],
                image1=fake.image_url(),
                image2=fake.image_url(),
                image3=fake.image_url(),
                image4=fake.image_url(),
                image5=fake.image_url(),
                price=fake.random_int(min=100, max=10000),
                currency='KES',
                quantity=fake.random_int(min=1, max=100),
                region=fake.city(),
                negotiable=fake.boolean(),
                sponsored=fake.boolean(),
                featured=fake.boolean(),
                new=fake.boolean(),
                most_sold=fake.boolean(),
                out_of_stock=fake.boolean(),
                product_serial=fake.uuid4(),
                owner=owner
            )
            num_created += 1
            self.stdout.write(f"Created appliance: {appliance.title}")

        self.stdout.write(f"Total appliances created: {num_created}")
  