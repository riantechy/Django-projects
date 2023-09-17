from django.db import models
from appliances.models import *
# Create your models here.
from django.db import models
from products.models import BaseProduct

class Other_Product_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Other_Product_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Other_Product_Category)
    

    def __str__(self):
        return self.name  
     
class Other_Product_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Other_Product_Sub_Category)

    def __str__(self):
        return self.name

class Other_Product_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Other_Product_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Other_Product_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Other_Product_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Other_Product_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS')
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name
        

class Other_Product(BaseProduct):
    title = models.CharField(max_length=150)
    category = models.ForeignKey( Other_Product_Category,related_name='otherproduct_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey( Other_Product_Sub_Category,related_name='otherproduct_subitems',  on_delete=models.CASCADE)
    type = models.ForeignKey( Other_Product_Type,related_name='otherproduct_subtypeitems',  on_delete=models.CASCADE)
    condition= models.ForeignKey( Other_Product_Condition, on_delete=models.CASCADE,blank=True, null=True)
    color= models.ForeignKey( Other_Product_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey( Other_Product_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey( Other_Product_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey( Other_Product_Material, on_delete=models.CASCADE,blank=True, null=True)
    dimensions = models.CharField(max_length=50,blank=True, null=True)
    weight = models.CharField(max_length=50,blank=True, null=True)
    voltage = models.CharField(max_length=50, blank=True, null=True)
    wattage = models.CharField(max_length=50, blank=True, null=True)
    per=models.ForeignKey(Per,on_delete=models.CASCADE, blank=True, null=True)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE, blank=True, null=True)
             


    def __str__(self) :
        return self.title
