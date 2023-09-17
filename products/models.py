from django.db import models
from business.models import Business
import uuid
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django_resized import ResizedImageField
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from locations.models import Locality

def upload_location(instance, filename):
    file_path = 'products/{owner__name}/{title}/{filename}'.format(
        owner__name=str(instance.owner.name), title=str(instance.title), filename=filename)
    return file_path



class BaseProduct(models.Model):   
    image1 = ResizedImageField(upload_to=upload_location, size=[600, 600], force_format="WEBP", quality=97,keep_meta=False, max_length=100)
    image2 = ResizedImageField(upload_to=upload_location, size=[600, 600], force_format="WEBP", quality=97,keep_meta=False, max_length=100,blank=True, null=True)
    image3 = ResizedImageField(upload_to=upload_location, size=[600, 600], force_format="WEBP", quality=97,keep_meta=False, max_length=100,blank=True, null=True)
    image4 = ResizedImageField(upload_to=upload_location, size=[600, 600], force_format="WEBP", quality=97,keep_meta=False, max_length=100,blank=True, null=True)
    image5 = ResizedImageField(upload_to=upload_location, size=[600, 600], force_format="WEBP", quality=97,keep_meta=False, max_length=100,blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=5, default='KES')   
    quantity = models.SmallIntegerField(default=1)
    locality = models.ForeignKey(Locality ,on_delete=models.CASCADE,blank=True, null=True)
    negotiable = models.BooleanField(default=False)    
    sponsored = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    most_sold = models.BooleanField(default=False)
    out_of_stock = models.BooleanField(default=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)     
    product_serial = models.CharField(max_length=255 ,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField( max_length= 500 ,blank=True, null=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Business, on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
    


    


@receiver(post_save)
def search_on_post_save(sender, instance,created, **kwargs):
    if issubclass(sender, BaseProduct):
         print(instance.slug)       
         if not instance.slug:
            slug_input = f"{instance.title}-{instance.category.name}-{instance.Locality}-{instance.subcategory}-{instance.type.name}"
            instance.slug = slugify(slug_input)            
            now = datetime.now()
            month = str(now.month).zfill(2)
            day = str(now.day).zfill(2)
            date_part = f"{day}{month}"
            # Generate random code
            random_code = uuid.uuid4().hex[:20]
            # Combine all parts to form the product serial number
            product_serial = f"{date_part}-{random_code}"
            instance.product_serial = product_serial
            # Save the instance
            instance.save()



         

    

    