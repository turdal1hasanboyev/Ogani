from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from apps.common.models import BaseModel
from apps.user.models import CustomUser
from apps.category.models import BlogCategory, BlogTag


class Blog(BaseModel):
    name = models.CharField(max_length=225, unique=True, db_index=True)
    slug = models.SlugField(unique=True, null=True,
                            blank=True, max_length=225, db_index=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs', null=True, blank=True)
    category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, related_name='blog_category')
    tags = models.ManyToManyField(
        BlogTag, blank=True, related_name='blog_tags')
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name='blog_author')
    review_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('blog-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.name}"
