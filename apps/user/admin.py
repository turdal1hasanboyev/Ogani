from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


admin.site.site_header = "Ogani Admin Panel"
admin.site.site_title = "Ogani Admin Panel"
admin.site.index_title = "Welcome to Ogani Admin Panel!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_superuser',
        'is_staff',
        'last_login',
        'date_joined',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    list_filter = (
        'is_active',
        'is_superuser',
        'is_staff',
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
        ("Personal Info", {
            'fields': ('first_name', 'last_name',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active',),
        }),
        ("Important Dates", {
            'fields': ('date_joined', 'last_login',),
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'fields': ('email', 'password1', 'password2',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active',),
        }),
    )
