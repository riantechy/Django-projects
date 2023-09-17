from django.db import models
from services.models import BaseService
# Create your models here.


class Other_Service_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Other_Service_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Other_Service_Category)   

    def __str__(self):
        return self.name  
     
class Other_Service_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Other_Service_Sub_Category)

    def __str__(self):
        return self.name

    
    
class Other_Service(BaseService):
    category = models.ForeignKey(Other_Service_Category,related_name='other_service_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Other_Service_Sub_Category,related_name='other_service_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Other_Service_Type,related_name='other_service_subtypeitems', on_delete=models.CASCADE)
    
 

    class Meta:
        verbose_name = 'Other_Service service'
        verbose_name_plural = 'Other_Service services'
