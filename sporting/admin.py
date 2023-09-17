from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import (
    Sport_Gooding_Category, 
    Sport_Gooding_Sub_Category, 
    Sport_Gooding_Type, 
    Sport_Gooding_Color, 
    Sport_Gooding_Size, 
    Sport_Gooding_Material, 
    Sport_Gooding_Condition, 
    Sport_Gooding_Brand, 
    Sport_Gooding
)

@admin.register(Sport_Gooding_Category)
class Sport_Gooding_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Sport_Gooding_Sub_Category)
class Sport_Gooding_Sub_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(Sport_Gooding_Type)
class Sport_Gooding_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(Sport_Gooding_Color)
class Sport_Gooding_ColorAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Sport_Gooding_Size)
class Sport_Gooding_SizeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Sport_Gooding_Material)
class Sport_Gooding_MaterialAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Sport_Gooding_Condition)
class Sport_Gooding_ConditionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Sport_Gooding_Brand)
class Sport_Gooding_BrandAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Sport_Gooding)
class Sport_GoodingAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',  'color', 'size', 'brand', 'material', 'condition')
    list_filter = ('category',  'color', 'size', 'brand', 'material', 'condition',  'sponsored', 'featured', 'new', 'most_sold', 'out_of_stock', 'negotiable', )