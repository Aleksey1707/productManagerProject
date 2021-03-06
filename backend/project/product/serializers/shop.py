from rest_framework import serializers

from product.models import Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = (
            'id',
            'name',
            'created',
            'modified',
        )
