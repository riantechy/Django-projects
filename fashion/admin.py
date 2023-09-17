from django.contrib import admin
from .models import Fashion, Fashion_Category, Fashion_Sub_Category, Fashion_Type, Fashion_Color, Fashion_Size, Fashion_Material, Fashion_Condition, Fashion_Brand
from import_export.admin import ImportExportMixin
class FashionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',  'color', 'size', 'brand', 'material', 'price', 'quantity')
    list_filter = ('category',  'color', 'size', 'brand', 'material', 'condition',
                   'featured', 'new', 'most_sold', 'out_of_stock', 'negotiable',)
class FashionCategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class FashionSubCategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )

class FashionTypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )

class FashionColorAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class FashionSizeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class FashionMaterialAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

class FashionConditionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'description')

class FashionBrandAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Fashion, FashionAdmin)
admin.site.register(Fashion_Category, FashionCategoryAdmin)
admin.site.register(Fashion_Sub_Category, FashionSubCategoryAdmin)
admin.site.register(Fashion_Type, FashionTypeAdmin)
admin.site.register(Fashion_Color, FashionColorAdmin)
admin.site.register(Fashion_Size, FashionSizeAdmin)
admin.site.register(Fashion_Material, FashionMaterialAdmin)
admin.site.register(Fashion_Condition, FashionConditionAdmin)
admin.site.register(Fashion_Brand, FashionBrandAdmin)
