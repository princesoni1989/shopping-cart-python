from .discounts import *


class ShippingZones(models.Model):
    name = models.CharField(max_length=20)
    countries = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    postal_code = models.IntegerField()

    class Meta:
        verbose_name_plural = "Shipping Zones"

    def __str__(self):
        return self.name


class ShippingMethods(models.Model):
    zone = models.ForeignKey(ShippingZones, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    max_order_price = models.FloatField()
    max_order_weight = models.FloatField()
    min_order_price = models.FloatField()
    min_order_weight = models.FloatField()
    price = models.FloatField()
    type = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Shipping Methods"

    def __str__(self):
        return self.name


status_options = (
    ('unshipped', 'Unshipped'),
    ('shipped', 'Shipped'),
    ('pending', 'Pending'),
    ('cancelled', 'Cancelled'),
    ('delivered', 'Delivered'),
)

