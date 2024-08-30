from django.db import models

from carpets.models import Material, Carpet
from users.models import CustomUser


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def get_total_price(self):
        if self.carpet is not None:
            return self.quantity * self.carpet.price
        elif self.material is not None:
            return self.quantity * self.material.price
