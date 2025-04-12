from django.db import models
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel


class ProductBanner(BaseModel):
    name = models.CharField(max_length=225, unique=True, db_index=True)
    image = models.ImageField(upload_to='banners', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    category = models.ForeignKey(
        'category.ProductCategory', on_delete=models.CASCADE,
        related_name='banner_category'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        limit_choices_to={"parent__isnull": True},
        null=True, blank=True,
        related_name="children")

    def __str__(self):
        return f"{self.name}"
