from rest_framework import serializers
from models.shipping import *


class ShippingZonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingZones
        fields = "__all__"


class ShippingMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethods
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(ShippingMethodsSerializer, self).to_representation(instance)
        rep['zone'] = instance.zone.name
        return rep

