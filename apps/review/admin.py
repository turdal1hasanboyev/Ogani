from django.contrib import admin
from .models import BlogReview


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
    list_filter = ('is_active', 'blog', 'user', 'rating',)
    search_fields = (
        'blog__name',
        'user__first_name',
        'user__last_name',
        'user__email',
    )
