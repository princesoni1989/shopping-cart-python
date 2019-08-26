from django.db import models
from django.contrib.auth.models import AbstractUser


class Customers(AbstractUser):
    is_seller = models.BooleanField(default=False)
    phone = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.first_name


class CustomerAddress(models.Model):
    users = models.ForeignKey(Customers, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=250)
    shipping_address = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "User Address"

    def __str__(self):
        return self.users


class SellerAddress(models.Model):
    users = models.ForeignKey(Customers, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.IntegerField()

    class Meta:
        verbose_name_plural = "Seller Address"

    def __str__(self):
        return self.users
