from django.db import models 
from products.models import BaseProduct
from appliances.models import *

class Gaming_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Gaming_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Gaming_Category)
    

    def __str__(self):
        return self.name  
     
class Gaming_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Gaming_Sub_Category)

    def __str__(self):
        return self.name

class Gaming_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Gaming_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Gaming_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Gaming_Condition(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Gaming_Genre(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Gaming_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS' ,blank=True, null=True)
    verified = models.BooleanField(default=False,blank=True, null=True)
        
class Gaming_Operating_System(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS',blank=True, null=True)
    

class Gaming_Ram_Metric(models.Model):
    name = models.CharField(max_length = 150)

    
class Gaming_Memory_Metric(models.Model):
    name = models.CharField(max_length = 150)
    
    

class Gaming_Memory_Type(models.Model):
    name = models.CharField(max_length = 150)

    

class Gaming_Screen_Size(models.Model):
    name = models.CharField(max_length = 150)

    

class Gaming_Weight_Metric(models.Model):
    name = models.CharField(max_length = 150)

   


class Gaming(BaseProduct):    
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Gaming_Category,related_name='gaming_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Gaming_Sub_Category,related_name='gaming_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Gaming_Type,related_name='gaming_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(Gaming_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Gaming_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Gaming_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Gaming_Material, on_delete=models.CASCADE,blank=True, null=True)
    model = models.CharField(max_length=150,blank=True, null=True)
    year = models.CharField(max_length=150,blank=True, null=True)
    condition = models.ForeignKey(Gaming_Condition, on_delete=models.CASCADE,blank=True, null=True)   
    platform = models.CharField(max_length=150,blank=True, null=True)
    genre = models.ForeignKey(Gaming_Genre, on_delete=models.CASCADE,blank=True, null=True)   
    multiplayer = models.BooleanField(default=False,blank=True, null=True)
    developer = models.CharField(max_length=150,blank=True, null=True)
    publisher = models.CharField(max_length=150,blank=True, null=True)
    system_requirements = models.TextField(blank=True, null=True)
    game_modes = models.CharField(max_length=150,blank=True, null=True)
    accessories_included = models.CharField(max_length=150,blank=True, null=True)
    language = models.CharField(max_length=150,blank=True, null=True) 
    per=models.ForeignKey(Per,on_delete=models.CASCADE)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE)

   
             


    def __str__(self) :
        return self.title




    class Meta:
        verbose_name = 'Gaming Product'
        verbose_name_plural = 'Gaming Products'


