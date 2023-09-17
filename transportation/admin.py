from django.contrib import admin
from .models import Transport, Transport_Category, Transport_Sub_Category, Transport_Type, Transport_Vehicle
from import_export.admin import ImportExportMixin

@admin.register(Transport_Category)
class TransportCategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Transport_Sub_Category)
class TransportSubCategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('category__name',)


@admin.register(Transport_Type)
class TransportTypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('subcategory__category__name',)

@admin.register(Transport)
class BaseServiceAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'price', 'is_mobile', 'negotiable', 'sponsored', 'featured', 'created_at', 'updated_at')
    list_filter = ('is_mobile', 'negotiable', 'sponsored', 'featured')
@admin.register(Transport_Vehicle)
class TransportVehicleAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ()