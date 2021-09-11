from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product import ProductSerializer, ProductListSerializer, ProductEditSerializer

CACHE_PAGE_SECONDS = 30


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related("product_states__shop").all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        elif self.action in ("create", "partial_update", "update"):
            return ProductEditSerializer
        return self.serializer_class

    @method_decorator(cache_page(CACHE_PAGE_SECONDS))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
