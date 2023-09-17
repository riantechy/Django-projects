from django.db import models

from products.models import BaseProduct

from appliances.models import *

class Health_Beauty_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Health_Beauty_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Health_Beauty_Category)
    

    def __str__(self):
        return self.name  
     
class Health_Beauty_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Health_Beauty_Sub_Category)

    def __str__(self):
        return self.name

    
class Health_Beauty_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Health_Beauty_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Health_Beauty_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Health_Beauty_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS',blank=True, null=True)
    verified = models.BooleanField(default=False,blank=True, null=True)
    def __str__(self):
        return self.name
    
class Health_Beauty_weight_Merits(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Health_Beauty_Volume_Merits(models.Model):
    name= models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
class Health_Beauty_Dimentions(models.Model):
    name = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

# class Health_Beauty_Fragrance(models.Model):
#     name = models.CharField(max_length = 150)
#     description=models.CharField(max_length=200)
#     def __str__(self):
#         return self. 
class Health_Beauty_Color(models.Model):
    name = models.CharField(max_length = 150)
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    
class Health_Beauty(BaseProduct):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Health_Beauty_Category,related_name='health_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Health_Beauty_Sub_Category,related_name='health_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Health_Beauty_Type,related_name='health_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(Health_Beauty_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Health_Beauty_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Health_Beauty_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Health_Beauty_Material, on_delete=models.CASCADE,blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    weight = models.ForeignKey(Health_Beauty_weight_Merits, on_delete=models.CASCADE,blank=True, null=True)
    volume = models.ForeignKey(Health_Beauty_Volume_Merits, on_delete=models.CASCADE,blank=True, null=True) 
    #fragrance = models.ForeignKey(Health_Beauty_Fragrance, on_delete=models.CASCADE,blank=True, null=True)
    packaging_type = models.CharField(max_length=50,blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    is_prescription_required = models.BooleanField(default=False)
    is_organic = models.BooleanField(default=False)
    is_cruelty_free = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_paraben_free = models.BooleanField(default=False)
    is_sulfate_free = models.BooleanField(default=False)
    is_phthalate_free = models.BooleanField(default=False)
    per=models.ForeignKey(Per,on_delete=models.CASCADE ,default=1)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title
