from rest_framework import serializers
from models.payments import *


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(PaymentsSerializer, self).to_representation(instance)
        rep['seller'] = instance.seller.users.first_name
        rep['orders'] = instance.orders.address.users.first_name
        return rep
