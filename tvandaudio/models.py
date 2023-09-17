# Create your models here.
from django.db import models
from products.models import BaseProduct
from appliances.models import *



class Tv_Audio_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Tv_Audio_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Tv_Audio_Category)
    

    def __str__(self):
        return self.name  
     
class Tv_Audio_Type(models.Model):
    name = models.CharField(max_length=150) 
    subcategory = models.ManyToManyField(Tv_Audio_Sub_Category)

    def __str__(self):
        return self.name

class Tv_Audio_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Tv_Audio_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Tv_Audio_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    

class Tv_Audio_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Tv_Audio_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
class Tv_Audio_Operating_System(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS')
   
    def __str__(self):
        return self.name

class Tv_Audio_Ram_Metric(models.Model):
    name = models.CharField(max_length = 150)

    
    def __str__(self):
        return self.name

class Tv_Audio_Memory_Metric(models.Model):
    name = models.CharField(max_length = 150)
    
    
    def __str__(self):
        return self.name

class Tv_Audio_Memory_Type(models.Model):
    name = models.CharField(max_length = 150)

   

    def __str__(self):
        return self.name

class Tv_Audio_Screen_Size(models.Model):
    name = models.CharField(max_length = 150)

    
    def __str__(self):
        return self.name

class Tv_Audio_Weight_Metric(models.Model):
    name = models.CharField(max_length = 150)

   
    def __str__(self):
        return self.name
    


class Tv_Audio(BaseProduct):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Tv_Audio_Category,related_name='tvaudio_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Tv_Audio_Sub_Category,related_name='tvaudio_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Tv_Audio_Type,related_name='tvaudio_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(Tv_Audio_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Tv_Audio_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Tv_Audio_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Tv_Audio_Material, on_delete=models.CASCADE,blank=True, null=True)
    display_type = models.CharField(max_length=150,blank=True, null=True)
    condition = models.ForeignKey(Tv_Audio_Condition, on_delete=models.CASCADE,blank=True, null=True)
    resolution = models.CharField(max_length=150,blank=True, null=True)
    refresh_rate = models.CharField(max_length=150,blank=True, null=True)    
    operating_system = models.ForeignKey(Tv_Audio_Operating_System, on_delete=models.CASCADE,blank=True, null=True)    
    weight = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True)
    weight_metrics=models.ForeignKey(Tv_Audio_Weight_Metric, on_delete=models.CASCADE,blank=True, null=True) 
    smart_tv = models.BooleanField(default=False)
    android_tv = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    sound_output = models.CharField(max_length=150,blank=True, null=True)
    surround_sound = models.BooleanField(default=False)
    voice_assistant = models.BooleanField(default=False)
    per=models.ForeignKey(Per,on_delete=models.CASCADE, blank=True, null=True)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.title
