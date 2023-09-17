from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import (Home_Office, Home_Office_Category, Home_Office_Sub_Category,
                     Home_Office_Type, Home_Office_Color, Home_Office_Size,
                     Home_Office_Material, Home_Office_Condition, Home_Office_Brand)

class Home_Office_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',  'condition', 'color', 'size', 'brand', 'material', 'dimensions', 'weight', 'voltage', 'wattage')
    list_filter = ('category',  'condition', 'color', 'size', 'brand', 'material','featured', 'new', 'most_sold', 'out_of_stock', 'negotiable',)

class Home_Office_Category_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Home_Office_Sub_Category_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )

class Home_Office_Type_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )

class Home_Office_Color_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Home_Office_Size_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Home_Office_Material_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Home_Office_Condition_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'description')

class Home_Office_Brand_Admin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'icon')

admin.site.register(Home_Office, Home_Office_Admin)
admin.site.register(Home_Office_Category, Home_Office_Category_Admin)
admin.site.register(Home_Office_Sub_Category, Home_Office_Sub_Category_Admin)
admin.site.register(Home_Office_Type, Home_Office_Type_Admin)
admin.site.register(Home_Office_Color, Home_Office_Color_Admin)
admin.site.register(Home_Office_Size, Home_Office_Size_Admin)
admin.site.register(Home_Office_Material, Home_Office_Material_Admin)
admin.site.register(Home_Office_Condition, Home_Office_Condition_Admin)
admin.site.register(Home_Office_Brand, Home_Office_Brand_Admin)
