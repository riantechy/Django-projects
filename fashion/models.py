# Create your models here.
from django.db import models
from products.models import BaseProduct
from  appliances.models import *

class Fashion_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Fashion_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Fashion_Category)
    

    def __str__(self):
        return self.name  
     
class Fashion_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Fashion_Sub_Category)

    def __str__(self):
        return self.name

class Fashion_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Fashion_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Fashion_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Fashion_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Fashion_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS')
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name
        
    
    
class Fashion(BaseProduct):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Fashion_Category,related_name='fashion_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Fashion_Sub_Category,related_name='fashion_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Fashion_Type,related_name='fashion_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(Fashion_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Fashion_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Fashion_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Fashion_Material, on_delete=models.CASCADE,blank=True, null=True)
    condition = models.ForeignKey(Fashion_Condition, on_delete=models.CASCADE,blank=True, null=True)
    per=models.ForeignKey(Per,on_delete=models.CASCADE)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



    class Meta:
        verbose_name = 'Fashion Product'
        verbose_name_plural = 'Fashion Products'
