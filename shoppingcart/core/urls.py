from django.urls import path
from . import views

urlpatterns = [
    # views_customers
    path('list-customers/', views.ListCreateCustomer.as_view(), name='list_create_customer'),
    path('update-customers/<int:pk>/', views.UpdateCustomer.as_view(), name='update_customer'),
    path('list-address/', views.ListAddress.as_view(), name='list_address'),
    path('update-address/<int:pk>/', views.UpdateAddress.as_view(), name='address_operations'),
    path('list-customer-address/', views.ListCustomerAddress.as_view(), name='list_customer_address'),
    path('update-customer-address/<int:pk>/', views.UpdateCustomerAddress.as_view(), name='update_customer_address'),
    path('list-seller-address/', views.ListSellerAddress.as_view(), name='list_seller_address'),
    path('update-seller-address/<int:pk>/', views.UpdateSellerAddress.as_view(), name='update_seller_address'),

    # views_products
    path('list-product-category/', views.ListProductCategory.as_view(), name='list_product_category'),
    path('update-product-category/<int:pk>/', views.UpdateProductCategory.as_view(), name='update_product_category'),
    path('list-products/', views.ListProducts.as_view(), name='list_products'),
    path('update-products/<int:pk>/', views.UpdateProducts.as_view(), name='update_products'),
    path('list-product-images/', views.ListProductImages.as_view(), name='list_product_images'),
    path('update-product-images/<int:pk>/', views.UpdateProductImages.as_view(), name='update_product_images'),
    path('list-product-colors/', views.ListProductColors.as_view(), name='list_product_colors'),
    path('update-product-colors/<int:pk>/', views.UpdateProductColors.as_view(), name='update_product_colors'),

    # views_discounts
    path('list-discounts/', views.ListDiscounts.as_view(), name='list_discounts'),
    path('update-discounts/<int:pk>/', views.UpdateDiscounts.as_view(), name='update_discounts'),

    # views_shippings
    path('list-shipping-zones/', views.ListShippingZones.as_view(), name='list_shipping_zones'),
    path('update-shipping-zones/<int:pk>/', views.UpdateShippingZones.as_view(), name='update_shipping_zones'),
    path('list-shipping-methods/', views.ListShippingMethods.as_view(), name='list_shipping_methods'),
    path('update-shipping-methods/<int:pk>/', views.UpdateShippingMethods.as_view(), name='update_shipping_methods'),

    # views_orders
    path('list-orders/', views.ListOrders.as_view(), name='list_orders'),
    path('update-orders/<int:pk>/', views.UpdateOrders.as_view(), name='update_orders'),

    # views_payments
    path('list-payments/', views.ListPayments.as_view(), name='list_payments'),
    path('update-payments/<int:pk>/', views.UpdatePayments.as_view(), name='update_payments'),

    # views_wishlist
    path('list-wishlist/', views.ListWishlist.as_view(), name='list_wishlist'),
    path('update-wishlist/<int:pk>/', views.UpdateWishlist.as_view(), name='update_wishlist'),
]
