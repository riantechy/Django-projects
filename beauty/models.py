from django.db import models
from services.models import BaseService
# Create your models here.


class Beauty_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Beauty_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Beauty_Category)
    

    def __str__(self):
        return self.name  
     
class Beauty_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Beauty_Sub_Category)

    def __str__(self):
        return self.name

    
         
    
class Beauty(BaseService):
    category = models.ForeignKey(Beauty_Category,related_name='transport_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Beauty_Sub_Category,related_name='transport_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Beauty_Type,related_name='transport_subtypeitems', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Beauty service'
        verbose_name_plural = 'Beauty services'
