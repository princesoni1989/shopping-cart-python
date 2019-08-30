from rest_framework import generics
from serializers.customers_serializer import *


class ListCreateCustomer(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class UpdateCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class ListAddress(generics.ListCreateAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressSerializer


class UpdateAddress(generics.RetrieveUpdateDestroyAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressSerializer


class ListCustomerAddress(generics.ListCreateAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer


class UpdateCustomerAddress(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer


class ListSellerAddress(generics.ListCreateAPIView):
    queryset = SellerAddress.objects.all()
    serializer_class = SellerAddressSerializer


class UpdateSellerAddress(generics.RetrieveUpdateDestroyAPIView):
    queryset = SellerAddress.objects.all()
    serializer_class = SellerAddressSerializer
