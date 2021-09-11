from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet

from product.models import Shop
from product.serializers.shop import ShopSerializer


CACHE_PAGE_SECONDS = 60


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    @method_decorator(cache_page(CACHE_PAGE_SECONDS))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
