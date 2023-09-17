from django.db import models
from appliances.models import  *
# Create your models here.
from django.db import models
from products.models import BaseProduct



class Sport_Gooding_Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Sport_Gooding_Sub_Category(models.Model):
    name = models.CharField(max_length = 150)    
    category = models.ManyToManyField(Sport_Gooding_Category)
    

    def __str__(self):
        return self.name  
     
class Sport_Gooding_Type(models.Model):
    name = models.CharField(max_length=150)
    subcategory = models.ManyToManyField(Sport_Gooding_Sub_Category)

    def __str__(self):
        return self.name

class Sport_Gooding_Color(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Sport_Gooding_Size(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Sport_Gooding_Material(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
class Sport_Gooding_Condition(models.Model):
    name = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Sport_Gooding_Brand(models.Model):
    name = models.CharField(max_length = 150)
    icon=models.ImageField(upload_to='ICONS',blank=True, null=True)
    verified = models.BooleanField(default=False)
        

class Sport_Gooding(BaseProduct):
    title = models.CharField(max_length = 150)    
    category = models.ForeignKey(Sport_Gooding_Category,related_name='sport_items', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Sport_Gooding_Sub_Category,related_name='sport_subitems', on_delete=models.CASCADE)
    type = models.ForeignKey(Sport_Gooding_Type,related_name='sport_subtypeitems', on_delete=models.CASCADE)
    color= models.ForeignKey(Sport_Gooding_Color, on_delete=models.CASCADE,blank=True, null=True)
    size= models.ForeignKey(Sport_Gooding_Size, on_delete=models.CASCADE,blank=True, null=True)
    brand= models.ForeignKey(Sport_Gooding_Brand, on_delete=models.CASCADE,blank=True, null=True)
    material= models.ForeignKey(Sport_Gooding_Material, on_delete=models.CASCADE,blank=True, null=True)
    condition= models.ForeignKey(Sport_Gooding_Condition, on_delete=models.CASCADE,blank=True, null=True)
    per=models.ForeignKey(Per,on_delete=models.CASCADE, blank=True, null=True)
    packaging=models.ForeignKey(Package ,on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Sporting Gooding Product'
        verbose_name_plural = 'Sporting Gooding Products'

             


    def __str__(self) :
        return self.title
