from django.db import models
from services.models import BaseService
# Create your models here.


class Cleaning_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Cleaning_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Cleaning_Category)
    

    def __str__(self):
        return self.name  
     
class Cleaning_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Cleaning_Sub_Category)

    def __str__(self):
        return self.name

    
class Cleaning_Vehicle(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name


        
    
    
class Cleaning(BaseService):
    category = models.ForeignKey(Cleaning_Category,related_name='transport_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Cleaning_Sub_Category,related_name='transport_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Cleaning_Type,related_name='transport_subtypeitems', on_delete=models.CASCADE)
    
    
 

    class Meta:
        verbose_name = 'Cleaning service'
        verbose_name_plural = 'Cleaning services'
