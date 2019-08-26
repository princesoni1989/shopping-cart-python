from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'is_superuser', 'is_staff'
                  'is_active', 'date_joined', 'last_login', 'is_seller',)


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'


class SellerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerAddress
        fields = ('company_name', 'address', 'city', 'state', 'country', 'postal_code',)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ()
