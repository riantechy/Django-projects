from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import (
    Health_Beauty,
    Health_Beauty_Category,
    Health_Beauty_Sub_Category,
    Health_Beauty_Type,
    Health_Beauty_Color,
    Health_Beauty_Size,
    Health_Beauty_Brand,
    Health_Beauty_Material,
    Health_Beauty_weight_Merits,
    Health_Beauty_Volume_Merits,
    #Health_Beauty_Fragrance,
    Health_Beauty_Condition,
)

class Health_Beauty_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',  'color', 'size', 'brand', 'material', 'weight', 'volume')
    list_filter = ('category',  'brand', 'material', 'weight', 'volume','featured','featured', 'new', 'most_sold', 'out_of_stock', 'negotiable',)

class Health_Beauty_Category_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Health_Beauty_Sub_Category_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Health_Beauty_Type_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )

class Health_Beauty_Color_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Health_Beauty_Size_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Health_Beauty_Brand_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Health_Beauty_Material_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Health_Beauty_weight_Merits_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Health_Beauty_Volume_Merits_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

# class Health_Beauty_Fragrance_Admin(ImportExportMixin,admin.ModelAdmin):
#     list_display = ('name',)

class Health_Beauty_Condition_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Health_Beauty, Health_Beauty_Admin)
admin.site.register(Health_Beauty_Category, Health_Beauty_Category_Admin)
admin.site.register(Health_Beauty_Sub_Category, Health_Beauty_Sub_Category_Admin)
admin.site.register(Health_Beauty_Type, Health_Beauty_Type_Admin)
admin.site.register(Health_Beauty_Color, Health_Beauty_Color_Admin)
admin.site.register(Health_Beauty_Size, Health_Beauty_Size_Admin)
admin.site.register(Health_Beauty_Brand, Health_Beauty_Brand_Admin)
admin.site.register(Health_Beauty_Material, Health_Beauty_Material_Admin)
admin.site.register(Health_Beauty_weight_Merits, Health_Beauty_weight_Merits_Admin)
admin.site.register(Health_Beauty_Volume_Merits, Health_Beauty_Volume_Merits_Admin)
#admin.site.register(Health_Beauty_Fragrance, Health_Beauty_Fragrance_Admin)
admin.site.register(Health_Beauty_Condition, Health_Beauty_Condition_Admin)
