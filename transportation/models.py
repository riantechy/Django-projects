from django.db import models
from services.models import BaseService
# Create your models here.


class Transport_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Transport_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Transport_Category)
    

    def __str__(self):
        return self.name  
     
class Transport_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Transport_Sub_Category)

    def __str__(self):
        return self.name

    
class Transport_Vehicle(models.Model):
    name = models.CharField(max_length = 150, blank=True, null=True)
    description = models.CharField(max_length = 150, blank=True, null=True)
    def __str__(self):
        return self.name


        
    
    
class Transport(BaseService):
    category = models.ForeignKey(Transport_Category,related_name='transport_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Transport_Sub_Category,related_name='transport_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Transport_Type,related_name='transport_subtypeitems', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Transport_Vehicle, on_delete=models.CASCADE)
    
 

    class Meta:
        verbose_name = 'Transport service'
        verbose_name_plural = 'Transport services'
