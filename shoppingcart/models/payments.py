from .orders import *


class Payments(models.Model):
    seller = models.ForeignKey(SellerAddress, on_delete=models.CASCADE)
    orders = models.OneToOneField(Orders, on_delete=models.CASCADE)
    gateway = models.CharField(max_length=20)
    created_date = models.DateField(auto_now_add=True)
    cc_name = models.CharField(max_length=30)
    cc_exp_month = models.IntegerField()
    cc_exp_year = models.IntegerField()
    cc_first_digits = models.IntegerField()
    cc_last_digits = models.IntegerField()

    class Meta:
        verbose_name_plural = "Payments"

    def __str__(self):
        return self.orders.address.users.first_name

