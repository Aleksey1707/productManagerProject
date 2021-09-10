from rest_framework import serializers

from product.models import Category


# ToDo Решил проблему N+1, выглядит немного костыльно, но не критично

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'created', 'modified', 'children')


CategoryListSerializer._declared_fields['children'] = CategoryListSerializer(
    many=True,
    source='get_children',
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('lft', 'rght', 'tree_id', )
