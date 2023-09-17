from django.db import models 
from products.models import BaseProduct
from appliances.models import *

class Phone_Tablet_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Phone_Tablet_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Phone_Tablet_Category)
    

    def __str__(self):
        return self.name  
     
class Phone_Tablet_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Phone_Tablet_Sub_Category)

    def __str__(self):
        return self.name

class Phone_Tablet_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Phone_Tablet_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Phone_Tablet_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
    
class Phone_Tablet_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Phone_Tablet_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS',blank=True, null=True)
    verified = models.BooleanField(default=False)
    def __str__(self):
       return self.name
        
class Phone_Tablet_Operating_System(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS',blank=True, null=True)
    class Meta:
        verbose_name = 'Phone and Tablet operating system'
        verbose_name_plural = 'Phone and Tablet operating systems'
    def __str__(self):
       return self.name

class Phone_Tablet_Ram_Metric(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Phone and Tablet Ram Metric'
        verbose_name_plural = 'Phone and Tablet Ram Metrics'
    def __str__(self):
      return self.name

class Phone_Tablet_Memory_Metric(models.Model):
    name = models.CharField(max_length = 150)
    
    class Meta:
        verbose_name = 'Phone and Tablet Memory Metric'
        verbose_name_plural = 'Phone and Tablet Memory Metrics'
    def __str__(self):
      return self.name

class Phone_Tablet_Memory_Type(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Phone and Tablet Memory Type'
        verbose_name_plural = 'Phone and Tablet Memory Types'
    

class Phone_Tablet_Screen_Size(models.Model):
    name = models.CharField(max_length = 150)
    
    class Meta:
        verbose_name = 'Phone and Tablet Screen Size'
        verbose_name_plural = 'Phone and Tablet Screen Sizes'
    

class Phone_Tablet_Weight_Metric(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Phone and Tablet Weight Metric'
        verbose_name_plural = 'Phone and Tablet Weight Metrics'
    def __str__(self):
      return self.name
    


class Phone_Tablet(BaseProduct):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Phone_Tablet_Category, related_name='phone_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Phone_Tablet_Sub_Category,related_name='phone_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Phone_Tablet_Type,related_name='phone_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(Phone_Tablet_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Phone_Tablet_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Phone_Tablet_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Phone_Tablet_Material, on_delete=models.CASCADE,blank=True, null=True)
    model = models.CharField(max_length=150,blank=True, null=True)
    condition = models.ForeignKey(Phone_Tablet_Condition, on_delete=models.CASCADE,blank=True, null=True)    
    processor = models.CharField(max_length=150,blank=True, null=True)
    ram= models.CharField(max_length=150,blank=True, null=True)
    ram_metrics = models.ForeignKey(Phone_Tablet_Ram_Metric, on_delete=models.CASCADE,blank=True, null=True)    
    storage = models.CharField(max_length=4,blank=True, null=True)
    storage_metrics = models.ForeignKey(Phone_Tablet_Memory_Metric, on_delete=models.CASCADE,blank=True, null=True)  
    screen_size = models.ForeignKey(Phone_Tablet_Screen_Size, on_delete=models.CASCADE,blank=True, null=True)
    operating_system = models.ForeignKey(Phone_Tablet_Operating_System, on_delete=models.CASCADE,blank=True, null=True)    
    weight = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True)
    weight_metrics=models.ForeignKey(Phone_Tablet_Weight_Metric, on_delete=models.CASCADE,blank=True, null=True)  
    per=models.ForeignKey(Per,on_delete=models.CASCADE, blank=True, null=True)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'Phone and Tablet Product'
        verbose_name_plural = 'Phone and Tablet Products'


             


    def __str__(self) :
        return self.title


