from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (
    Per,Package,
    Appliance_Category, Appliance_Sub_Category, Appliance_Type,
    Appliance_Color, Appliance_Size, Appliance_Material,
    Appliance_Condition, Appliance_Brand, Appliance,
)

class ApplianceAdmin(ImportExportModelAdmin):
    list_display = ('title', 'power_rating', 'category',  'color', 'size', 'brand', 'material', 'condition')
    list_filter = ('category',  'color', 'size', 'brand',  'condition',  'sponsored', 'featured', 'new', 'most_sold', 'out_of_stock', 'negotiable', )

class ApplianceCategoryAdmin(ImportExportModelAdmin):
    list_display = ('name',)

class ApplianceSubCategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', )

class ApplianceTypeAdmin(ImportExportModelAdmin):
    list_display = ('name' ,)

    
class ApplianceColorAdmin(ImportExportModelAdmin):
    list_display = ('name',)

class ApplianceSizeAdmin(ImportExportModelAdmin):
    list_display = ('name',)

class ApplianceMaterialAdmin(ImportExportModelAdmin):
    list_display = ('name',)

class ApplianceConditionAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description')

class ApplianceBrandAdmin(ImportExportModelAdmin):
    list_display = ('name', 'icon')
class PerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description')

class PackageAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Per, PerAdmin)
admin.site.register(Package, PackageAdmin)

admin.site.register(Appliance, ApplianceAdmin)
admin.site.register(Appliance_Category, ApplianceCategoryAdmin)
admin.site.register(Appliance_Sub_Category, ApplianceSubCategoryAdmin)
admin.site.register(Appliance_Type, ApplianceTypeAdmin)
admin.site.register(Appliance_Color, ApplianceColorAdmin)
admin.site.register(Appliance_Size, ApplianceSizeAdmin)
admin.site.register(Appliance_Material, ApplianceMaterialAdmin)
admin.site.register(Appliance_Condition, ApplianceConditionAdmin)
admin.site.register(Appliance_Brand, ApplianceBrandAdmin)

