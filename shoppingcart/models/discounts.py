from .products import *


class Discounts(models.Model):
    product = models.ManyToManyField(Products)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    usage_limit = models.PositiveIntegerField()
    is_active = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    discount_value = models.FloatField()
    min_amount_spent = models.FloatField()
    apply_once_per_order = models.BooleanField(default=True)
    apply_once_per_customer = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return self.name
