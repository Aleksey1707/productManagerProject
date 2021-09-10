from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views.category import CategoryViewSet
from product.views.product import ProductViewSet
from product.views.product_state import ProductStateViewSet
from product.views.shop import ShopViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'products', ProductViewSet, basename="products")
router.register(r'shops', ShopViewSet, basename="shops")
router.register(r'product_states', ProductStateViewSet, basename="product_states")

urlpatterns = [
    path('v1/', include(router.urls))
]
