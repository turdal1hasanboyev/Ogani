from django.contrib import admin
from .models import WishList


class WishListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'session_id',
        'user',
        'product',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
    )


admin.site.register(WishList, WishListAdmin)
