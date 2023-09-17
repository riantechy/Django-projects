from django.db import models
from business.models import Business# Create your models here.
from locations.models import *
import uuid
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django_resized import ResizedImageField
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_location(instance, filename):
    file_path = 'services/{owner__name}/{title}/-{filename}'.format(
        owner__name=str(instance.owner.name), title=str(instance.title), filename=filename)
    return file_path



class BaseService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image1 = ResizedImageField(upload_to=upload_location, size=[600, 600], force_format="WEBP", quality=97,keep_meta=False,  max_length=100)
    image2 = ResizedImageField(upload_to=upload_location, size=[600, 600], force_format="WEBP", quality=97,keep_meta=False, max_length=100,blank=True, null=True)
    image3 = ResizedImageField(upload_to=upload_location, size=[600, 600], force_format="WEBP", quality=97,keep_meta=False, max_length=100,blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length = 5 , default='KES')    
    is_mobile = models.BooleanField(default=False)  
    negotiable = models.BooleanField(default=False)    
    sponsored=models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    locality = models.ForeignKey(Locality ,on_delete=models.CASCADE,blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],null=True,blank=True) 
    service_serial = models.CharField(max_length=255 ,blank=True, null=True)
    slug = models.SlugField(max_length=500,blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(Business,on_delete=models.CASCADE)

    class Meta:
        abstract = True
 
    def __str__(self):
        return self.title




@receiver(post_save)
def search_on_post_save(sender, instance,created, **kwargs):
    if issubclass(sender, BaseService):
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
            # Combine all parts to form the service serial number
            service_serial = f"{date_part}-{random_code}"
            instance.service_serial = service_serial
            # Save the instance
            instance.save()



         

    

    