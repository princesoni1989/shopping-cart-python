from .payments import *


class Wishlist(models.Model):
    user = models.OneToOneField(Customers, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class WishlistItems(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Wishlist Items"

    def __str__(self):
        return self.wishlist
