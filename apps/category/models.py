from django.db import models
from django.utils.text import slugify
from apps.common.models import BaseModel


class BlogCategory(BaseModel):
    name = models.CharField(max_length=225, db_index=True, unique=True)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class BlogTag(BaseModel):
    name = models.CharField(max_length=225, db_index=True, unique=True)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class ProductCategory(BaseModel):
    name = models.CharField(max_length=225, db_index=True, unique=True)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class ProductTag(BaseModel):
    name = models.CharField(max_length=225, db_index=True, unique=True)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
