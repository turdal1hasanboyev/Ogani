from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=225, db_index=True, unique=True)
    slug = models.SlugField(unique=True, null=True,
                            blank=True, max_length=225, db_index=True)
    banner = models.ForeignKey(
        'banner.ProductBanner', on_delete=models.SET_NULL, null=True, related_name='product_banner')
    description = RichTextField(null=True, blank=True)
    views_count = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    percentage = models.IntegerField(default=0)
    category = models.ForeignKey(
        'category.ProductCategory', on_delete=models.CASCADE,
        related_name="product_category"
    )
    tags = models.ManyToManyField(
        'category.ProductTag', blank=True, related_name="product_tags")
    author = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='product_author')

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("product-detail", kwargs={"slug": self.slug})

    @property
    def discount(self):
        if self.percentage:
            return self.price - (self.price * self.percentage) / 100
        return self.price

    @property
    def reviews_count(self):
        return self.product_review.count()

    def __str__(self):
        return f"{self.name}"


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='products', null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name}"
