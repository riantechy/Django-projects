from django.contrib import admin
from .models import Beauty, Beauty_Category, Beauty_Sub_Category, Beauty_Type
from import_export.admin import ImportExportMixin

@admin.register(Beauty_Category)
class BeautyCategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Beauty_Sub_Category)
class BeautySubCategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('category__name',)


@admin.register(Beauty_Type)
class BeautyTypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('subcategory__category__name',)

@admin.register(Beauty)
class BaseServiceAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'price', 'is_mobile', 'negotiable', 'sponsored', 'featured', 'created_at', 'updated_at')
    list_filter = ('is_mobile', 'negotiable', 'sponsored', 'featured')