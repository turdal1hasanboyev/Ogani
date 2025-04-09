from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SubEmail(BaseModel):
    sub_email = models.EmailField(
        max_length=150, unique=True, db_index=True, null=True, blank=True)

    def __str__(self):
        return f"{self.sub_email}"
