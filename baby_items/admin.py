from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import (BabyProduct, BabyProduct_Category, BabyProduct_Sub_Category, BabyProduct_Type, 
                     BabyProduct_Color, BabyProduct_Size, BabyProduct_Material, BabyProduct_Condition, BabyProduct_Brand)

class BabyProductAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('title', 'category',  'color', 'size', 'brand', 'material',  'featured')
    list_filter = ('category',  'color', 'size', 'brand',  'condition',  'sponsored', 'featured', 'new', 'most_sold', 'out_of_stock', 'negotiable', )
    search_fields = ('title', 'additional_features')

class BabyProduct_CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)

class BabyProduct_Sub_CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', )

class BabyProduct_TypeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', )

class BabyProduct_ColorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)

class BabyProduct_SizeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)

class BabyProduct_MaterialAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)

class BabyProduct_ConditionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'description')

class BabyProduct_BrandAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(BabyProduct, BabyProductAdmin)
admin.site.register(BabyProduct_Category, BabyProduct_CategoryAdmin)
admin.site.register(BabyProduct_Sub_Category, BabyProduct_Sub_CategoryAdmin)
admin.site.register(BabyProduct_Type, BabyProduct_TypeAdmin)
admin.site.register(BabyProduct_Color, BabyProduct_ColorAdmin)
admin.site.register(BabyProduct_Size, BabyProduct_SizeAdmin)
admin.site.register(BabyProduct_Material, BabyProduct_MaterialAdmin)
admin.site.register(BabyProduct_Condition, BabyProduct_ConditionAdmin)
admin.site.register(BabyProduct_Brand, BabyProduct_BrandAdmin)
