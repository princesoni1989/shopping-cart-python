from rest_framework import generics
from serializers.products_serializer import *


class ListProductCategory(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class UpdateProductCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ListProducts(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class UpdateProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ListProductImages(generics.ListCreateAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer


class UpdateProductImages(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesSerializer


class ListProductColors(generics.ListCreateAPIView):
    queryset = ProductColors.objects.all()
    serializer_class = ProductColorsSerializer


class UpdateProductColors(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductColors.objects.all()
    serializer_class = ProductColorsSerializer
