from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import (
    Other_Product,
    Other_Product_Category,
    Other_Product_Sub_Category,
    Other_Product_Type,
    Other_Product_Color,
    Other_Product_Size,
    Other_Product_Material,
    Other_Product_Condition,
    Other_Product_Brand,
)

class Other_Product_Admin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'condition',
        'color',
        'size',
        'brand',
        'material',
        'price',
        'quantity',
        'owner',
    ]
    search_fields = [
        'title',
        'category__name',
        'subcategory__name',
        'type__name',
        'condition__name',
        'color__name',
        'size__name',
        'brand__name',
        'material__name',
    ]
    list_filter = [
        'category',
        'condition',
        'color',
        'size',
        'brand',
        'material',
        'featured',
        'new',
        'most_sold',
        'out_of_stock',
        'negotiable',
    ]
    list_editable = ['price', 'quantity']

class Other_Product_Category_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']

class Other_Product_Sub_Category_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']

class Other_Product_Type_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']

class Other_Product_Color_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']

class Other_Product_Size_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']

class Other_Product_Material_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']

class Other_Product_Condition_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']

class Other_Product_Brand_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Other_Product, Other_Product_Admin)
admin.site.register(Other_Product_Category, Other_Product_Category_Admin)
admin.site.register(Other_Product_Sub_Category, Other_Product_Sub_Category_Admin)
admin.site.register(Other_Product_Type, Other_Product_Type_Admin)
admin.site.register(Other_Product_Color, Other_Product_Color_Admin)
admin.site.register(Other_Product_Size, Other_Product_Size_Admin)
admin.site.register(Other_Product_Material, Other_Product_Material_Admin)
admin.site.register(Other_Product_Condition, Other_Product_Condition_Admin)
admin.site.register(Other_Product_Brand, Other_Product_Brand_Admin)
