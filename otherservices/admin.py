from django.contrib import admin
from .models import Other_Service_Category, Other_Service_Sub_Category, Other_Service_Type, Other_Service
from import_export.admin import ImportExportMixin


class Other_ServiceAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'price', 'currency', 'is_mobile', 'locality', 'negotiable', 'sponsored', 'featured', 'category', )
    list_filter = ('created_at', 'updated_at', 'is_mobile', 'negotiable', 'sponsored', 'featured', 'category', )

admin.site.register(Other_Service_Category)
admin.site.register(Other_Service_Sub_Category)
admin.site.register(Other_Service_Type)
admin.site.register(Other_Service, Other_ServiceAdmin)
