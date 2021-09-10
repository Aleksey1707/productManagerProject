from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category import CategorySerializer, CategoryListSerializer


# TODO нужен рефакторинг


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # @method_decorator(cache_page(60))
    # @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = Category.objects.get_cached_trees()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CategoryListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CategoryListSerializer(queryset, many=True)
        return Response(serializer.data)
