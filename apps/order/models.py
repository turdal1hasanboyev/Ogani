from django.db import models
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel


class Order(BaseModel):
    STATUS = (
        (0, 'New'),
        (1, 'Completed'),
        (2, 'Canceled'),
    )
    status = models.IntegerField(choices=STATUS, default=0)
    user = models.ForeignKey(
        'user.CustomUser', on_delete=models.SET_NULL, null=True, related_name="orders")
    phone_number = models.CharField(max_length=15, db_index=True)
    full_name = models.CharField(max_length=225, db_index=True)
    notes = RichTextField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def total(self):
        return sum([item.total for item in self.items.all()])

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"
