from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'status',
        'user',
        'full_name',
        'phone_number',
        'total',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'status',
        'is_active',
    )
    search_fields = (
        'full_name',
        'phone_number',
    )
