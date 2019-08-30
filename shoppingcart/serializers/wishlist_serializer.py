from rest_framework import serializers
from models.wishlist import *


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItems
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(WishlistSerializer, self).to_representation(instance)
        rep['user'] = instance.user.first_name
        product_list = list()

        for item in instance.products.all():
            product_list.append(item.name)
            rep['products'] = product_list
        return rep
