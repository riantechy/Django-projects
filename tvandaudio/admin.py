from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import (
    Tv_Audio_Category, 
    Tv_Audio_Sub_Category, 
    Tv_Audio_Type, 
    Tv_Audio_Color, 
    Tv_Audio_Size, 
    Tv_Audio_Material, 
    Tv_Audio_Condition, 
    Tv_Audio_Brand, 
    Tv_Audio_Operating_System,
    Tv_Audio_Ram_Metric, 
    Tv_Audio_Memory_Metric, 
    Tv_Audio_Memory_Type,
    Tv_Audio_Screen_Size, 
    Tv_Audio_Weight_Metric, 
    Tv_Audio
)

class ImportExportAdminMixin(ImportExportMixin, admin.ModelAdmin):
    pass

class Tv_Audio_Category_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Sub_Category_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Type_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Color_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Size_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Material_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Condition_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Brand_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Operating_System_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Ram_Metric_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Memory_Metric_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Memory_Type_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Screen_Size_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Weight_Metric_Admin(ImportExportAdminMixin):
    list_display = ['name']

class Tv_Audio_Admin(ImportExportAdminMixin):
    list_display = ['title', 'category',  'color', 'size', 'brand',
                    'material', 'display_type', 'condition', 'resolution', 'refresh_rate',
                    'operating_system', 'weight', 'weight_metrics', 'smart_tv', 'android_tv',
                    'wifi', 'bluetooth', 'sound_output', 'surround_sound', 'voice_assistant']
    list_filter = ['category',  'color', 'size', 'brand', 'material', 
                   'condition', 'operating_system', 'weight_metrics', 'smart_tv', 'android_tv', 
                   'wifi', 'bluetooth', 'surround_sound', 'voice_assistant']

admin.site.register(Tv_Audio_Category, Tv_Audio_Category_Admin)
admin.site.register(Tv_Audio_Sub_Category, Tv_Audio_Sub_Category_Admin)
admin.site.register(Tv_Audio_Type, Tv_Audio_Type_Admin)
admin.site.register(Tv_Audio_Color, Tv_Audio_Color_Admin)
admin.site.register(Tv_Audio_Size, Tv_Audio_Size_Admin)
admin.site.register(Tv_Audio_Material, Tv_Audio_Material_Admin)
admin.site.register(Tv_Audio_Condition, Tv_Audio_Condition_Admin)
admin.site.register(Tv_Audio_Brand, Tv_Audio_Brand_Admin)
admin.site.register(Tv_Audio_Operating_System ,Tv_Audio_Operating_System_Admin)
admin.site.register(Tv_Audio_Ram_Metric ,Tv_Audio_Ram_Metric_Admin)
admin.site.register(Tv_Audio_Memory_Metric ,Tv_Audio_Memory_Metric_Admin)
admin.site.register(Tv_Audio_Memory_Type ,Tv_Audio_Memory_Type_Admin)
admin.site.register(Tv_Audio_Screen_Size ,Tv_Audio_Screen_Size_Admin)
admin.site.register(Tv_Audio_Weight_Metric ,Tv_Audio_Weight_Metric_Admin)
admin.site.register(Tv_Audio, Tv_Audio_Admin)
