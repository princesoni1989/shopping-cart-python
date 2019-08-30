from rest_framework import serializers
from models.orders import *


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(OrdersSerializer, self).to_representation(instance)
        rep['address'] = instance.address.address.billing_address
        rep['products'] = instance.products.name
        rep['discount'] = instance.discount.name
        rep['shipping_method'] = instance.shipping_method.name
        return rep
