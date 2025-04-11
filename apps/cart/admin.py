from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_completed',
        'session_id',
        'ip_address',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_completed',
        'is_active',
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cart',
        'order',
        'product',
        'quantity',
        'total',
        'main_total',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
    )
