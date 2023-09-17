from django.db import models
from services.models import BaseService
# Create your models here.


class Catering_Event_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Catering_Event_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Catering_Event_Category)
    

    def __str__(self):
        return self.name  
     
class Catering_Event_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Catering_Event_Sub_Category)

    def __str__(self):
        return self.name

    
class Catering_Event_Vehicle(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name


        
    
    
class Catering_Event(BaseService):
    category = models.ForeignKey(Catering_Event_Category,related_name='transport_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Catering_Event_Sub_Category,related_name='transport_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Catering_Event_Type,related_name='transport_subtypeitems', on_delete=models.CASCADE)

 

    class Meta:
        verbose_name = 'Catering_Event service'
        verbose_name_plural = 'Catering_Event services'
