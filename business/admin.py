from django.contrib import admin
from .models import Business
from import_export.admin import ImportExportMixin

@admin.register(Business)
class BusinessAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'website', 'industry', 'employee_count', 'bs_reg_number', 'is_verified', 'is_top_rated')
    list_filter = ( 'is_verified', 'is_top_rated')
    search_fields = ('name' , 'owner__id_number')

    def phone_number(self, obj):
        return obj.phone_number if obj.phone_number else '-'
    phone_number.short_description = 'Phone Number'
