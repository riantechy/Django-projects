from django.contrib import admin
from .models import Mechanic_Category, Mechanic_Sub_Category, Mechanic_Type, Mechanic
from import_export.admin import ImportExportMixin
class MechanicAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'price', 'currency', 'is_mobile', 'locality', 'negotiable', 'sponsored', 'featured', 'category', )
    list_filter = ('created_at', 'updated_at', 'is_mobile', 'negotiable', 'sponsored', 'featured', 'category', )

class MechanicCategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class MechanicSubCategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class MechanicTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Mechanic_Category, MechanicCategoryAdmin)
admin.site.register(Mechanic_Sub_Category, MechanicSubCategoryAdmin)
admin.site.register(Mechanic_Type, MechanicTypeAdmin)
admin.site.register(Mechanic, MechanicAdmin)


