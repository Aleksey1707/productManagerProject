from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category import CategorySerializer, CategoryListSerializer

# ToDo в идеале этот параметр необходимо вынести либо на административную панель,
#  либо в переменные окружения, но точно не хардкодом здесь
CACHE_PAGE_SECONDS = 60


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @method_decorator(cache_page(CACHE_PAGE_SECONDS))
    def list(self, request, *args, **kwargs):
        # ToDo Здесь имеется проблема с рекурсией дочерних категорий,
        #  а именно ломается drf-yasg, когда пытается составить схему
        #  Поэтому если реализовывать по правильному метод `get_serializer_class`,
        #  то drf-yasg подцепляет сериализатор и падает
        #  Поэтому пришлось указать этот сериализатор прямо в этой функции, чтоб dfr-yasg до него не добрался
        queryset = Category.objects.get_cached_trees()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CategoryListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CategoryListSerializer(queryset, many=True)
        return Response(serializer.data)
