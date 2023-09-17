from django.db import models 
from products.models import BaseProduct
from appliances.models import *

class Computing_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Computing_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Computing_Category)
    

    def __str__(self):
        return self.name  
     
class Computing_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Computing_Sub_Category)

    def __str__(self):
        return self.name

class Computing_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Computing_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Computing_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    

    
class Computing_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Computing_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS',blank=True, null=True)
    verified = models.BooleanField(default=False,blank=True, null=True)
        
class Computing_Operating_System(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS',blank=True, null=True)
    class Meta:
        verbose_name = 'Computing operating system'
        verbose_name_plural = 'Computing operating systems'

class Computing_Ram_Metric(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Computing Ram Metric'
        verbose_name_plural = 'Computing Ram Metrics'

class Computing_Memory_Metric(models.Model):
    name = models.CharField(max_length = 150)
    
    class Meta:
        verbose_name = 'Computing Memory Metric'
        verbose_name_plural = 'Computing Memory Metrics'

class Computing_Memory_Type(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Computing Memory Type'
        verbose_name_plural = 'Computing Memory Types'

class Computing_Screen_Size(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Computing Screen Size'
        verbose_name_plural = 'Computing Screen Sizes'

class Computing_Weight_Metric(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Computing Weight Metric'
        verbose_name_plural = 'Computing Weight Metrics'
    


class Computing(BaseProduct):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Computing_Category, related_name='computing_items',on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Computing_Sub_Category,related_name='computing_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Computing_Type,related_name='computing_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(Computing_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Computing_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Computing_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Computing_Material, on_delete=models.CASCADE,blank=True, null=True)
    model = models.CharField(max_length=150,blank=True, null=True)
    condition = models.ForeignKey(Computing_Condition, on_delete=models.CASCADE,blank=True, null=True)    
    processor = models.CharField(max_length=150,blank=True, null=True)
    ram= models.CharField(max_length=150,blank=True, null=True)
    ram_metrics = models.ForeignKey(Computing_Ram_Metric, on_delete=models.CASCADE,blank=True, null=True)
    storage_type = models.ForeignKey(Computing_Memory_Type, on_delete=models.CASCADE,blank=True, null=True)    
    storage = models.CharField(max_length=4,blank=True, null=True)
    storage_metrics = models.ForeignKey(Computing_Memory_Metric, on_delete=models.CASCADE,blank=True, null=True)  
    graphics_card = models.CharField(max_length=150,blank=True, null=True)
    screen_size = models.ForeignKey(Computing_Screen_Size, on_delete=models.CASCADE,blank=True, null=True)
    operating_system = models.ForeignKey(Computing_Operating_System, on_delete=models.CASCADE,blank=True, null=True)    
    weight = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True)
    weight_metrics=models.ForeignKey(Computing_Weight_Metric, on_delete=models.CASCADE,blank=True, null=True)  
    per=models.ForeignKey(Per,on_delete=models.CASCADE)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE)

   
             


    def __str__(self) :
        return self.title



    class Meta:
        verbose_name = 'Computing Product'
        verbose_name_plural = 'Computing  Products'

