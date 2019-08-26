# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
#
#
# class Customers(AbstractUser):
#     is_seller = models.BooleanField(default=False)
#     phone = models.IntegerField()
#
#     class Meta:
#         verbose_name_plural = "Customers"
#
#     def __str__(self):
#         return self.first_name
#
#
# class CustomerAddress(models.Model):
#     users = models.ForeignKey(Customers, on_delete=models.CASCADE)
#     billing_address = models.CharField(max_length=250)
#     shipping_address = models.CharField(max_length=250)
#
#     class Meta:
#         verbose_name_plural = "User Address"
#
#     def __str__(self):
#         return self.users
#
#
# class SellerAddress(models.Model):
#     users = models.ForeignKey(Customers, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=100, blank=False)
#     address = models.CharField(max_length=250)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#     postal_code = models.IntegerField()
#
#     class Meta:
#         verbose_name_plural = "Seller Address"
#
#     def __str__(self):
#         return self.users
#
#
# class ProductCategory(models.Model):
#     category = models.CharField(max_length=50)
#     description = models.TextField(max_length=100)
#     background_image = models.ImageField(upload_to='product/', default='product/default.png')
#     seo_title = models.CharField(max_length=20)
#     seo_description = models.TextField(max_length=100)
#
#     class Meta:
#         verbose_name_plural = "Product Category"
#
#     def __str__(self):
#         return self.category
#
#
# class Products(models.Model):
#     category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
#     user = models.ForeignKey(Customers, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, blank=False)
#     description = models.TextField(max_length=100)
#     price = models.FloatField()
#     publication_date = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#     quantity = models.PositiveIntegerField(default=1)
#     is_published = models.BooleanField(default=False)
#     seo_title = models.CharField(max_length=20)
#     seo_description = models.TextField(max_length=100)
#     tax = models.FloatField()
#     weight = models.FloatField()
#
#     class Meta:
#         verbose_name_plural = "Products"
#
#     def __str__(self):
#         return self.name
#
#
# class ProductImages(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product/', default='product/default.png')
#
#
# class Discounts(models.Model):
#     name = models.CharField(max_length=20)
#     code = models.CharField(max_length=20)
#     usage_limit = models.PositiveIntegerField()
#     is_active = models.BooleanField(default=False)
#     start_date = models.DateField(auto_now_add=True)
#     end_date = models.DateField()
#     discount_value = models.FloatField()
#     min_amount_spent = models.FloatField()
#     apply_once_per_order = models.BooleanField(default=True)
#     apply_once_per_customer = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name_plural = 'Discounts'
#
#     def __str__(self):
#         return self.name
#
#
# class ShippingZones(models.Model):
#     name = models.CharField(max_length=20)
#     countries = models.CharField(max_length=20)
#     city = models.CharField(max_length=20)
#     area = models.CharField(max_length=20)
#     postal_code = models.IntegerField()
#
#     class Meta:
#         verbose_name_plural = "Shipping Zones"
#
#     def __str__(self):
#         return self.name
#
#
# class ShippingMethods(models.Model):
#     zone = models.ManyToManyField(ShippingZones)
#     name = models.CharField(max_length=20)
#     max_order_price = models.FloatField()
#     max_order_weight = models.FloatField()
#     min_order_price = models.FloatField()
#     min_order_weight = models.FloatField()
#     price = models.FloatField()
#     type = models.CharField(max_length=20)
#
#     class Meta:
#         verbose_name_plural = "Shipping Methods"
#
#     def __str__(self):
#         return self.name
#
#
# status_options = (
#     ('unshipped', 'Unshipped'),
#     ('shipped', 'Shipped'),
#     ('pending', 'Pending'),
#     ('cancelled', 'Cancelled'),
#     ('delivered', 'Delivered'),
# )
#
#
# class Orders(models.Model):
#     users = models.ForeignKey(Customers, on_delete=models.CASCADE)
#     address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
#     discount = models.ForeignKey(Discounts, on_delete=models.CASCADE)
#     products = models.ForeignKey(Products, on_delete=models.CASCADE)
#     shipping_method = models.ForeignKey(ShippingMethods, on_delete=models.CASCADE)
#     tracking_number = models.IntegerField()
#     created_date = models.DateField(auto_now_add=True)
#     total_net = models.FloatField()
#     status = models.CharField(choices=status_options, max_length=20)
#     refund_requested = models.BooleanField(default=False)
#     refund_granted = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name_plural = 'Orders'
#
#     def __str__(self):
#         return self.users
#
#
# class Payments(models.Model):
#     seller = models.ForeignKey(SellerAddress, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
#     orders = models.OneToOneField(Orders, on_delete=models.CASCADE)
#     gateway = models.CharField(max_length=20)
#     created_date = models.DateField(auto_now_add=True)
#     cc_name = models.CharField(max_length=30)
#     cc_exp_month = models.IntegerField()
#     cc_exp_year = models.IntegerField()
#     cc_first_digits = models.IntegerField()
#     cc_last_digits = models.IntegerField()
#
#     class Meta:
#         verbose_name_plural = "Payments"
#
#     def __str__(self):
#         return self.user
#
#
# class Wishlist(models.Model):
#     user = models.OneToOneField(Customers, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user
#
#
# class WishlistItems(models.Model):
#     wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
#     products = models.ForeignKey(Products, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = "Wishlist Items"
#
#     def __str__(self):
#         return self.wishlist
