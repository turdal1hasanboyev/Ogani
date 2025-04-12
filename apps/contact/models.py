from django.db import models
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
