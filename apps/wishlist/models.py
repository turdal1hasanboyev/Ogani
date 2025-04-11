from django.db import models
from ..common.models import BaseModel


class WishList(BaseModel):
    session_id = models.CharField(max_length=225, blank=True, null=True)
    user = models.ForeignKey(
        'user.CustomUser', on_delete=models.SET_NULL, null=True, related_name='wishlist_user')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, related_name='wishlist_product')

    def __str__(self):
        return f"{self.product.name}"
