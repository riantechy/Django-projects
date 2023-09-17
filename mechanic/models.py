from django.db import models
from services.models import BaseService
# Create your models here.


class Mechanic_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Mechanic_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Mechanic_Category)
    

    def __str__(self):
        return self.name  
     
class Mechanic_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Mechanic_Sub_Category)

    def __str__(self):
        return self.name

    
    
class Mechanic(BaseService):
    category = models.ForeignKey(Mechanic_Category,related_name='transport_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Mechanic_Sub_Category,related_name='transport_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Mechanic_Type,related_name='transport_subtypeitems', on_delete=models.CASCADE)
    
 

    class Meta:
        verbose_name = 'Mechanic service'
        verbose_name_plural = 'Mechanic services'
