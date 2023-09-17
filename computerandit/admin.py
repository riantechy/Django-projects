from django.contrib import admin
from .models import Computer_It, Computer_It_Category, Computer_It_Sub_Category, Computer_It_Type, Computer_It_Vehicle
from import_export.admin import ImportExportMixin

class Computer_ItAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'price', 'locality', 'created_at')
    list_filter = ('locality', 'created_at', 'featured')
    search_fields = ('title', 'description', 'locality')



class Computer_It_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)


class Computer_It_Sub_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )


class Computer_It_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )


class Computer_It_VehicleAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Computer_It, Computer_ItAdmin)
admin.site.register(Computer_It_Category, Computer_It_CategoryAdmin)
admin.site.register(Computer_It_Sub_Category, Computer_It_Sub_CategoryAdmin)
admin.site.register(Computer_It_Type, Computer_It_TypeAdmin)
admin.site.register(Computer_It_Vehicle, Computer_It_VehicleAdmin)
