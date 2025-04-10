from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'category',
        'author',
        'review_count',
        'is_active',
        "created_at",
        "updated_at",
    )
    list_filter = (
        'is_active',
        'category',
        'author',
    )
    search_fields = (
        'name',
        'category__name',
        'author__first_name',
        'author__last_name',
        'author__email',
    )
    prepopulated_fields = {'slug': ('name',)}
