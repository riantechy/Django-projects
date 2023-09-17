from django.db import models

# Create your models here.
from django.db import  models
from  appliances.models import *
from products.models import BaseProduct


class Home_Office_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Home_Office_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Home_Office_Category)
    

    def __str__(self):
        return self.name  
     
class Home_Office_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Home_Office_Sub_Category)

    def __str__(self):
        return self.name

class Home_Office_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Home_Office_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Home_Office_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
    
class Home_Office_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Home_Office_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS',blank=True, null=True)
    verified = models.BooleanField(default=False,blank=True, null=True)

    def __str__(self):
        return self.name
        
    
class Home_Office(BaseProduct):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Home_Office_Category,related_name='home_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Home_Office_Sub_Category,related_name='home_subitems',  on_delete=models.CASCADE)
    type = models.ForeignKey(Home_Office_Type,related_name='home_subtypeitems',  on_delete=models.CASCADE)
    condition= models.ForeignKey(Home_Office_Condition, on_delete=models.CASCADE,blank=True, null=True)
    color= models.ForeignKey(Home_Office_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Home_Office_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Home_Office_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Home_Office_Material, on_delete=models.CASCADE,blank=True, null=True)
    dimensions = models.CharField(max_length=50,blank=True, null=True)
    weight = models.CharField(max_length=50,blank=True, null=True)
    voltage = models.CharField(max_length=50, blank=True, null=True)
    wattage = models.CharField(max_length=50, blank=True, null=True)
    per=models.ForeignKey(Per,on_delete=models.CASCADE)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE)

   
             


    def __str__(self) :
        return self.title



  
