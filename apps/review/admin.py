from django.contrib import admin
from .models import BlogReview, ProductReview


@admin.register(BlogReview)
class BlogReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'blog',
        'rating',
        'is_active',
        "created_at",
        "updated_at",
    )
    list_filter = ('is_active',)


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'user',
        'rating',
        'is_active',
        "created_at",
        "updated_at",
    )
    list_filter = ('is_active',)
