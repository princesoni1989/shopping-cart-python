from .shipping import *


class Orders(models.Model):
    address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discounts, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    shipping_method = models.ForeignKey(ShippingMethods, on_delete=models.CASCADE)
    tracking_number = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    total_net = models.FloatField()
    status = models.CharField(choices=status_options, max_length=20)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.address.users.first_name
