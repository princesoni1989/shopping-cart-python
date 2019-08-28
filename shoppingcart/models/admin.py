from django.contrib import admin
from .customers import *
from .products import *
from .discounts import *
from .shipping import *
from .orders import *
from .payments import *
from .wishlist import *

# Register your models here.
admin.site.register(Customers)
admin.site.register(Addresses)
admin.site.register(CustomerAddress)
admin.site.register(SellerAddress)

admin.site.register(ProductCategory)
admin.site.register(Products)
admin.site.register(ProductImages)
admin.site.register(ProductColors)

admin.site.register(Discounts)

admin.site.register(ShippingZones)
admin.site.register(ShippingMethods)

admin.site.register(Orders)

admin.site.register(Payments)

admin.site.register(WishlistItems)
