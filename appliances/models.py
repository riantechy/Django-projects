from django.db import models
from products.models import BaseProduct
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from datetime import datetime
import uuid
class Appliance_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Appliance_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Appliance_Category)
    
    def __str__(self):
        return self.name  
     
class Appliance_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Appliance_Sub_Category)

    def __str__(self):
        return self.name
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
class Appliance_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Appliance_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Appliance_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Appliance_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Appliance_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS')
    verified = models.BooleanField(default=False)

    def __str__(self):
         return self.name
           
class Per(models.Model):
    name = models.CharField(max_length = 150)
    description=models.TextField()
    def __str__(self) :
        return self.name

class Package(models.Model):
    name=models.CharField(max_length= 150)
    description = models.TextField()
    def __str__(self) :
        return self.name
          
    
class Appliance(BaseProduct):
    title=models.CharField(max_length=100)
    power_rating=models.CharField(max_length=100)
    category = models.ForeignKey(Appliance_Category, related_name='appliance_items',on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Appliance_Sub_Category,related_name='appliance_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Appliance_Type,related_name='appliance_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(Appliance_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Appliance_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Appliance_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Appliance_Material, on_delete=models.CASCADE,blank=True, null=True)
    condition = models.ForeignKey(Appliance_Condition, on_delete=models.CASCADE,blank=True, null=True) 
    per=models.ForeignKey(Per,on_delete=models.CASCADE)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE)

    def __str__(self):
         return self.title


