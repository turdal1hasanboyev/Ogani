from django.db import models
from apps.common.models import BaseModel


class Cart(BaseModel):
    is_completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=225, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    @property
    def total(self):
        if self.cart_items.count() == 0:
            return 0
        return sum([item.total for item in self.cart_items.all()])

    @property
    def main_total(self):
        if self.cart_items.count() == 0:
            return 0
        return sum([item.main_total for item in self.cart_items.all()])

    @property
    def items_count(self):
        if not self.cart_items:
            return 0
        return self.cart_items.count()

    def __str__(self):
        return f"{self.session_id}"


class CartItem(BaseModel):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    order = models.ForeignKey(
        'order.Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, related_name='cart_product')
    quantity = models.IntegerField(default=1)

    @property
    def total(self):
        return self.product.discount * self.quantity

    @property
    def main_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name}"
