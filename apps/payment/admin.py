from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'amount',
        'order',
        'payment_method',
        'status',
        'transaction_id',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'status',
        'payment_method',
    )
