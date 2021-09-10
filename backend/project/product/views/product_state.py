from rest_framework.viewsets import ModelViewSet

from product.models import ProductState
from product.serializers.product_state import ProductStateSerializer


class ProductStateViewSet(ModelViewSet):
    queryset = ProductState.objects.all()
    serializer_class = ProductStateSerializer
