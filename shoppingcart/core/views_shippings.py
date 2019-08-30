from rest_framework import generics
from serializers.shipping_serializer import *


class ListShippingZones(generics.ListCreateAPIView):
    queryset = ShippingZones.objects.all()
    serializer_class = ShippingZonesSerializer


class UpdateShippingZones(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingZones.objects.all()
    serializer_class = ShippingZonesSerializer


class ListShippingMethods(generics.ListCreateAPIView):
    queryset = ShippingMethods.objects.all()
    serializer_class = ShippingMethodsSerializer


class UpdateShippingMethods(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingMethods.objects.all()
    serializer_class = ShippingMethodsSerializer
