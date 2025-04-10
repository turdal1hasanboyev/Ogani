from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.common.models import BaseModel


class BlogReview(BaseModel):
    user = models.ForeignKey(
        'user.CustomUser', on_delete=models.CASCADE, related_name='blogreview_user')
    blog = models.ForeignKey(
        'blog.Blog', on_delete=models.CASCADE, related_name='blogreview_blog')
    review = models.TextField(null=True, blank=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.blog}"
