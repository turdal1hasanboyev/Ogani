from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = (
        'id',
        'name',
        'banner',
        'views_count',
        'price',
        'percentage',
        'discount',
        'category',
        'author',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}
