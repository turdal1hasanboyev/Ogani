from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_active', 'created_at', 'updated_at',)
    list_filter = ('is_active',)
    search_fields = ('name', 'email',)
