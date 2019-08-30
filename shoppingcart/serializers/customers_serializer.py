from rest_framework import serializers
from models.customers import *


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'phone', 'is_superuser', 'is_staff',
                  'is_active', 'date_joined', 'last_login', 'is_seller',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = "__all__"


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(CustomerAddressSerializer, self).to_representation(instance)
        rep['users'] = instance.users.first_name
        rep['address'] = instance.address.billing_address
        return rep


class SellerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerAddress
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(SellerAddressSerializer, self).to_representation(instance)
        rep['users'] = instance.users.first_name
        return rep

