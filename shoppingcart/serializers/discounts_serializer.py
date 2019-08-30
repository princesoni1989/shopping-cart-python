from rest_framework import serializers
from models.discounts import *


class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = "__all__"
