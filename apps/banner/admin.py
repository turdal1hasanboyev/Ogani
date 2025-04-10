from django.contrib import admin
from .models import ProductBanner


@admin.register(ProductBanner)
class ProductBannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'category',
        'parent',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active',)
    search_fields = ('name',)
