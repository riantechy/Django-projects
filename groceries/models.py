from django.db import models
from products.models import BaseProduct
from  appliances.models  import *
# Create your models here.
from business.models import Business


class Grocery_Category(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Grocery Category'
        verbose_name_plural = 'Grocery Categories'


    def __str__(self) :
        return self.name

class Grocery_Sub_Category(models.Model):
    category = models.ManyToManyField(Grocery_Category)    
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Grocery Sub-Category'
        verbose_name_plural = 'Grocery Sub-Categories'

    def __str__(self) :
        return self.name
    
class Grocery_Type(models.Model):
    name = models.CharField(max_length = 150)
    subcategory = models.ManyToManyField(Grocery_Sub_Category)
    
    class Meta:
        verbose_name = 'Grocery Type '
        verbose_name_plural = 'Grocery Types'

    def __str__(self) :
        return self.name
 

    
class Grocery_Metrics(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name


    
class Grocery_Condition(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Grocery_Color(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name
    
# class VerifiedProductManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(featured=True)


    

class Grocery(BaseProduct):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Grocery_Category,related_name='grocery_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Grocery_Sub_Category,related_name='grocery_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Grocery_Type,related_name='grocery_subtypeitems', on_delete=models.CASCADE)
    metrics= models.ForeignKey(Grocery_Metrics, on_delete=models.CASCADE,blank=True, null=True)
    condition = models.ForeignKey(Grocery_Condition, on_delete=models.CASCADE,blank=True, null=True)
    color = models.ForeignKey(Grocery_Color, on_delete=models.CASCADE,blank=True, null=True)
    per=models.ForeignKey(Per,on_delete=models.CASCADE)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE)
   
    # objects = VerifiedProductManager() # Custom manager for verified products.


   
             


    def __str__(self) :
        return self.title




   