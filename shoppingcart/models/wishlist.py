from .payments import *


class WishlistItems(models.Model):
    user = models.OneToOneField(Customers, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)

    class Meta:
        verbose_name_plural = "Wishlist Items"

    def __str__(self):
        return self.user.first_name
