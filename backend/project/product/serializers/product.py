from rest_framework import serializers

from product.models import Product
from product.serializers.product_state import ProductStateSerializer, ProductStateEditSerializer


class ProductListSerializer(serializers.ModelSerializer):

    product_states = ProductStateSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'product_states',
            'created',
            'modified',
        )


class ProductEditSerializer(serializers.ModelSerializer):

    product_states = ProductStateEditSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'product_states',
            'created',
            'modified',
        )


class ProductSerializer(serializers.ModelSerializer):
    product_states = ProductStateSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'product_states',
            'created',
            'modified',
        )
