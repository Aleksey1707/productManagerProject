from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet

from product.models import ProductState
from product.serializers.product_state import ProductStateSerializer, ProductStateEditSerializer

# Состояние товара изменяется в разы чаще, чем те же категории, продукты и магазины
CACHE_PAGE_SECONDS = 10


class ProductStateViewSet(ModelViewSet):
    queryset = ProductState.objects.select_related("shop").all()
    serializer_class = ProductStateSerializer

    def get_serializer_class(self):
        if self.action in ("create", "partial_update", "update"):
            return ProductStateEditSerializer
        return self.serializer_class

    @method_decorator(cache_page(CACHE_PAGE_SECONDS))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
