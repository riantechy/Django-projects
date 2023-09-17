from django.contrib import admin
# Register your models here.
from .models import County,SubCounty,Locality

class CountyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class SubCountyAdmin(admin.ModelAdmin):
    list_display =("name","county")
    search_fields = ("name","county")
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class LocalityAdmin(admin.ModelAdmin):
    list_display = ('name','subcounty','county','is_city')
    search_fields = ('name','subcounty' )
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()





admin.site.register(County,CountyAdmin)
admin.site.register(SubCounty,SubCountyAdmin)
admin.site.register( Locality,LocalityAdmin)

