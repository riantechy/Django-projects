from django.db import models
from services.models import BaseService
# Create your models here.


class Computer_It_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Computer_It_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Computer_It_Category)
    

    def __str__(self):
        return self.name  
     
class Computer_It_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Computer_It_Sub_Category)

    def __str__(self):
        return self.name

    
class Computer_It_Vehicle(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name


        
    
    
class Computer_It(BaseService):
    category = models.ForeignKey(Computer_It_Category,related_name='transport_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Computer_It_Sub_Category,related_name='transport_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Computer_It_Type,related_name='transport_subtypeitems', on_delete=models.CASCADE)

 

    class Meta:
        verbose_name = 'Computer_It service'
        verbose_name_plural = 'Computer_It services'
