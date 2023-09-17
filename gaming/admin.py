from django.contrib import admin
from .models import Gaming, Gaming_Category, Gaming_Sub_Category, Gaming_Type, Gaming_Color, Gaming_Size, Gaming_Material, Gaming_Condition, Gaming_Genre, Gaming_Brand, Gaming_Operating_System, Gaming_Ram_Metric, Gaming_Memory_Metric, Gaming_Memory_Type, Gaming_Screen_Size, Gaming_Weight_Metric
from import_export.admin import ImportExportMixin
# Register your models here.

class GamingAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'category',  'color', 'size', 'brand', 'material', 'model', 'year', 'condition', 'platform', 'genre', 'multiplayer', 'developer', 'publisher', 'sponsored', 'featured', 'new', 'most_sold', 'out_of_stock', 'price', 'quantity', 'locality', 'negotiable', 'owner',)
    list_filter = ('category',  'color', 'size', 'brand', 'material', 'condition', 'genre', 'multiplayer', 'sponsored', 'featured', 'new', 'most_sold', 'out_of_stock', 'negotiable', )
    
class Gaming_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_Sub_CategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    
class Gaming_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    
class Gaming_ColorAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_SizeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_MaterialAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_ConditionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_GenreAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'description',)
    
class Gaming_BrandAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'icon',)
    
class Gaming_Operating_SystemAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', 'icon',)
    
class Gaming_Ram_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_Memory_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_Memory_TypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_Screen_SizeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    
class Gaming_Weight_MetricAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Gaming, GamingAdmin)
admin.site.register(Gaming_Category, Gaming_CategoryAdmin)
admin.site.register(Gaming_Sub_Category, Gaming_Sub_CategoryAdmin)
admin.site.register(Gaming_Type, Gaming_TypeAdmin)
admin.site.register(Gaming_Color, Gaming_ColorAdmin)
admin.site.register(Gaming_Size, Gaming_SizeAdmin)
admin.site.register(Gaming_Material, Gaming_MaterialAdmin)
admin.site.register(Gaming_Condition, Gaming_ConditionAdmin)
admin.site.register(Gaming_Genre, Gaming_GenreAdmin)
admin.site.register(Gaming_Brand, Gaming_BrandAdmin)
admin.site.register(Gaming_Operating_System, Gaming_Operating_SystemAdmin)
admin.site.register(Gaming_Ram_Metric, Gaming_Ram_MetricAdmin)
admin.site.register(Gaming_Memory_Metric, Gaming_Memory_MetricAdmin)
admin.site.register(Gaming_Memory_Type, Gaming_Memory_TypeAdmin)
admin.site.register(Gaming_Screen_Size, Gaming_Screen_SizeAdmin)
admin.site.register(Gaming_Weight_Metric, Gaming_Weight_MetricAdmin)
