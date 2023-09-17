from django.contrib import admin
from .models import (Computing, Computing_Category, Computing_Sub_Category, Computing_Type, 
                     Computing_Color, Computing_Size, Computing_Material, Computing_Condition, 
                     Computing_Brand, Computing_Operating_System, Computing_Ram_Metric, 
                     Computing_Memory_Metric, Computing_Memory_Type, Computing_Screen_Size, 
                     Computing_Weight_Metric)
from import_export.admin import ImportExportMixin


class ComputingAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',  'color', 'size', 'brand', 'material', 'model', 'condition', 
                    'processor', 'ram', 'ram_metrics', 'storage_type', 'storage', 'storage_metrics', 'graphics_card', 
                    'screen_size', 'operating_system', 'weight', 'weight_metrics', 'featured')
    list_filter = ('category',  'color', 'size', 'brand', 'material', 'condition', 'ram_metrics', 
                   'storage_type', 'storage_metrics', 'screen_size', 'operating_system', 'weight_metrics', 'featured','featured', 'new', 'most_sold', 'out_of_stock', 'negotiable',)


class Computing_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_Sub_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )

class Computing_ColorAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_SizeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_MaterialAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_ConditionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'description')

class Computing_BrandAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_Operating_SystemAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_Ram_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_Memory_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_Memory_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_Screen_SizeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class Computing_Weight_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Computing, ComputingAdmin)
admin.site.register(Computing_Category, Computing_CategoryAdmin)
admin.site.register(Computing_Sub_Category, Computing_Sub_CategoryAdmin)
admin.site.register(Computing_Type, Computing_TypeAdmin)
admin.site.register(Computing_Color, Computing_ColorAdmin)
admin.site.register(Computing_Size, Computing_SizeAdmin)
admin.site.register(Computing_Material, Computing_MaterialAdmin)
admin.site.register(Computing_Condition, Computing_ConditionAdmin)
admin.site.register(Computing_Brand, Computing_BrandAdmin)
admin.site.register(Computing_Operating_System, Computing_Operating_SystemAdmin)
admin.site.register(Computing_Ram_Metric, Computing_Ram_MetricAdmin)
admin.site.register(Computing_Memory_Metric, Computing_Memory_MetricAdmin)
admin.site.register(Computing_Memory_Type, Computing_Memory_TypeAdmin)
admin.site.register(Computing_Screen_Size, Computing_Screen_SizeAdmin)
admin.site.register(Computing_Weight_Metric, Computing_Weight_MetricAdmin)
