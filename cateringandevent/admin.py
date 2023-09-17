from import_export.admin import ImportExportMixin
from django.contrib import admin
from .models import (
    Catering_Event,
    Catering_Event_Category,
    Catering_Event_Sub_Category,
    Catering_Event_Type,
    Catering_Event_Vehicle,
)

class Catering_EventAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',   'price', 'currency', 'is_mobile', 'negotiable', 'sponsored', 'featured', 'created_at', 'updated_at')
    list_filter = ('category',    'sponsored', 'featured')
    search_fields = ('title', 'description', )
    ordering = ('-created_at',)

class Catering_Event_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Catering_Event_Sub_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'category__name')
    

class Catering_Event_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'subcategory__name')
    list_filter = ('subcategory__category',)



admin.site.register(Catering_Event, Catering_EventAdmin)
admin.site.register(Catering_Event_Category, Catering_Event_CategoryAdmin)
admin.site.register(Catering_Event_Sub_Category, Catering_Event_Sub_CategoryAdmin)
admin.site.register(Catering_Event_Type, Catering_Event_TypeAdmin)

