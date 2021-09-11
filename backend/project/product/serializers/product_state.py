from rest_framework import serializers

from product.models import ProductState
from product.serializers.shop import ShopSerializer


class ProductStateEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductState
        fields = (
            'id',
            'quantity',
            'price',
            'product',
            'shop',
            'created',
            'modified',
        )


class ProductStateSerializer(serializers.ModelSerializer):

    shop = ShopSerializer()

    class Meta:
        model = ProductState
        fields = (
            'id',
            'quantity',
            'price',
            'product',
            'shop',
            'created',
            'modified',
        )
