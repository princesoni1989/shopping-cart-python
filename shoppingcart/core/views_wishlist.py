from rest_framework import generics
from serializers.wishlist_serializer import *


class ListWishlist(generics.ListCreateAPIView):
    queryset = WishlistItems.objects.all()
    serializer_class = WishlistSerializer


class UpdateWishlist(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishlistItems.objects.all()
    serializer_class = WishlistSerializer
