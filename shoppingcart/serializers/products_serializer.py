from rest_framework import serializers
from models.products import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(ProductsSerializer, self).to_representation(instance)
        rep['category'] = instance.category.category
        return rep


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"


class ProductColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColors
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(ProductColorsSerializer, self).to_representation(instance)
        product_list = list()
        for item in instance.product.all():
            product_list.append(item.name)
            rep['product'] = product_list
        return rep
