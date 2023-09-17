from django.contrib import admin
from .models import (
    Phone_Tablet_Category, Phone_Tablet_Sub_Category, Phone_Tablet_Type, Phone_Tablet_Color,
    Phone_Tablet_Size, Phone_Tablet_Material, Phone_Tablet_Condition, Phone_Tablet_Brand,
    Phone_Tablet_Operating_System, Phone_Tablet_Ram_Metric, Phone_Tablet_Memory_Metric,
    Phone_Tablet_Memory_Type, Phone_Tablet_Screen_Size, Phone_Tablet_Weight_Metric, Phone_Tablet
)
from import_export.admin import ImportExportMixin

@admin.register(Phone_Tablet_Category)
class Phone_Tablet_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Sub_Category)
class Phone_Tablet_Sub_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Type)
class Phone_Tablet_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Color)
class Phone_Tablet_ColorAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Size)
class Phone_Tablet_SizeAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Material)
class Phone_Tablet_MaterialAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Condition)
class Phone_Tablet_ConditionAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Brand)
class Phone_Tablet_BrandAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Operating_System)
class Phone_Tablet_Operating_SystemAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Ram_Metric)
class Phone_Tablet_Ram_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Memory_Metric)
class Phone_Tablet_Memory_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Memory_Type)
class Phone_Tablet_Memory_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Screen_Size)
class Phone_Tablet_Screen_SizeAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet_Weight_Metric)
class Phone_Tablet_Weight_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    pass


@admin.register(Phone_Tablet)
class Phone_TabletAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',  'color', 'size', 'brand', 'model', 'condition', 'price', 'currency', 'quantity', 'locality', 'negotiable', 'sponsored', 'featured')
    list_filter = ('category',  'color', 'size', 'brand', 'material', 'condition', 'ram_metrics', 'storage_metrics', 'screen_size', 'operating_system', 'weight_metrics', 'negotiable', 'sponsored', 'featured', 'new', 'most_sold', 'out_of_stock', 'negotiable',)
    search_fields = ('title', 'model')
