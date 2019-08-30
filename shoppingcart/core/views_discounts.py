from rest_framework import generics
from serializers.discounts_serializer import *


class ListDiscounts(generics.ListCreateAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer


class UpdateDiscounts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer
