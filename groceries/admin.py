from django.contrib import admin
from .models import Grocery, Grocery_Category, Grocery_Sub_Category, Grocery_Type
from import_export.admin import ImportExportMixin

@admin.register(Grocery)
class GroceryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'locality', 'negotiable', 'sponsored', 'featured', 'new', 'most_sold', 'out_of_stock', 'product_serial', 'owner', 'updated', 'created')
    list_filter = ('category',  'color',   'condition', 'sponsored', 'featured', 'new', 'most_sold', 'out_of_stock', 'negotiable', )
    search_fields = ('title', 'locality', 'owner__name')
    list_per_page = 25
    ordering = ['-created']

@admin.register(Grocery_Category)
class GroceryCategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Grocery_Sub_Category)
class GrocerySubCategoryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', 'category__name')

@admin.register(Grocery_Type)
class GroceryTypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
