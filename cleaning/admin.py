from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import (
    Cleaning,
    Cleaning_Category,
    Cleaning_Sub_Category,
    Cleaning_Type,
    Cleaning_Vehicle,
)

class CleaningAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',  'price', 'currency', 'is_mobile' , 'negotiable', 'sponsored', 'featured', 'created_at', 'updated_at')
    list_filter = ('category',   'sponsored', 'featured')
    search_fields = ('title', 'description', )
    ordering = ('-created_at',)

class Cleaning_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Cleaning_Sub_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

class Cleaning_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'subcategory__name')
    list_filter = ('subcategory__category',)

class Cleaning_VehicleAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(Cleaning, CleaningAdmin)
admin.site.register(Cleaning_Category, Cleaning_CategoryAdmin)
admin.site.register(Cleaning_Sub_Category, Cleaning_Sub_CategoryAdmin)
admin.site.register(Cleaning_Type, Cleaning_TypeAdmin)
admin.site.register(Cleaning_Vehicle, Cleaning_VehicleAdmin)
