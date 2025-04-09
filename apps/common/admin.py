from django.contrib import admin
from .models import SubEmail


@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sub_email',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'sub_email',
    )
    list_filter = (
        'is_active',
    )
