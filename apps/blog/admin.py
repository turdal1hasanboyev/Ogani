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
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
