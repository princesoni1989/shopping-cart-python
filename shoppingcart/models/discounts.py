from .products import *


class Discounts(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    usage_limit = models.PositiveIntegerField()
    is_active = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)
    discount_value = models.FloatField()
    min_amount_spent = models.FloatField()
    apply_once_per_order = models.BooleanField(default=False)
    apply_once_per_customer = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return self.name
