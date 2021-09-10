from rest_framework import serializers

from product.models import ProductState


class ProductStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductState
        fields = '__all__'
