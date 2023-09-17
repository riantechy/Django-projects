from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, ActivationCode, Customer, Merchant, Admin, Support

admin.site.site_header = 'JIKONNECTSOKO'
admin.site.site_title = 'JIkONNECTSOKO'
admin.site.index_title = 'Admin panel'

class BaseAccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'phone_number', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = []
    list_filter = ['is_staff','is_superuser', 'is_active','is_admin','is_customer','is_merchant','is_support']
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone_number', 'password', 'date_joined',)
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions',)
        }),
        ('Fundamental Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
        ('plartform Roles', {
            'classes': ('collapse',),
            'fields': ('is_admin','is_customer','is_merchant','is_support')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2',)
        }),
    )

class AccountAdmin(BaseAccountAdmin):
   def has_module_permission(self, request):
        if not request.user.is_superuser:
            return False
        return super().has_module_permission(request)
 

class OtherAdmin(BaseAccountAdmin):
    list_display = ('email', 'username', 'phone_number', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login',) 

    filter_horizontal = []
    list_filter = ['is_staff', 'is_active','is_admin','is_customer','is_merchant','is_support']
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone_number', 'password', 'date_joined',)
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups',)
        }),
        ('Fundamental Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active','is_staff')
        }),
        ('plartform Roles', {
            'classes': ('collapse',),
            'fields': ('is_admin','is_customer','is_merchant','is_support')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2',)
        }),
    )
class SupportAdmin(BaseAccountAdmin):
    list_display = ('email', 'username', 'phone_number', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login',) 

    filter_horizontal = []
    list_filter = ['is_staff', 'is_active','is_admin','is_customer','is_merchant','is_support']
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone_number', 'password', 'date_joined',)
        }),
        ('Fundamental Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active',)
        }),
        ('plartform Roles', {
            'classes': ('collapse',),
            'fields': ('is_customer','is_merchant',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2',)
        }),
    )

class CustomerAdmin(BaseAccountAdmin):
    list_display = ('email', 'username', 'phone_number', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login',) 

    filter_horizontal = []
    list_filter = ['is_staff', 'is_active','is_admin','is_customer','is_merchant','is_support']
    fieldsets = (
        (None, {
        
            'fields': ('username', 'email', 'phone_number', 'date_joined',)
        }),       
        ('Fundamental Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active',)
        }),
        ('plartform Roles', {
            'classes': ('collapse',),
            'fields': ('is_customer',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2',)
        }),
    )


class MerchantAdmin(BaseAccountAdmin):
    list_display = ('email', 'username', 'phone_number', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login',) 

    filter_horizontal = []
    list_filter = ['is_staff', 'is_active','is_admin','is_customer','is_merchant','is_support']

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone_number', 'password', 'date_joined',)
        }),
        ('Fundamental Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active',)
        }),
        ('plartform Roles', {
            'classes': ('collapse',),
            'fields': ('is_merchant',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone_number', 'password1', 'password2',)
        }),
    )


class ActivationCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'created_at', 'updated_at')
    search_fields = ['email']
    readonly_fields = ('created_at','updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(ActivationCode, ActivationCodeAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Admin, OtherAdmin)
admin.site.register(Support, SupportAdmin)
