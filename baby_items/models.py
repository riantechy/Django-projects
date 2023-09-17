from django.db import models

# Create your models here.
from django.db import models
from products.models import BaseProduct
from appliances.models import *
class BabyProduct_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class BabyProduct_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(BabyProduct_Category)
    

    def __str__(self):
        return self.name  
     
class BabyProduct_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(BabyProduct_Sub_Category)

    def __str__(self):
        return self.name

class BabyProduct_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class BabyProduct_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class BabyProduct_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class BabyProduct_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class BabyProduct_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        

    

class BabyProduct(BaseProduct):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(BabyProduct_Category,related_name='babyproducts_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(BabyProduct_Sub_Category,related_name='babyproducts_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(BabyProduct_Type,related_name='babyproducts_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(BabyProduct_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(BabyProduct_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(BabyProduct_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(BabyProduct_Material, on_delete=models.CASCADE,blank=True, null=True)
    additional_features = models.TextField(blank=True, null=True)
    condition = models.ForeignKey(BabyProduct_Condition, on_delete=models.CASCADE,blank=True, null=True)
    per=models.ForeignKey(Per,on_delete=models.CASCADE)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    


    
    
