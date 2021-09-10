from rest_framework.viewsets import ModelViewSet

from product.models import Shop
from product.serializers.shop import ShopSerializer


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
