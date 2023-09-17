from django.contrib import admin
# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','id_number','first_name','last_name',)
    search_fields = ['id_number']
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Profile, ProfileAdmin)

