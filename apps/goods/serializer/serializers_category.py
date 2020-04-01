from django.db.models.functions import Lower, Concat, LTrim
from rest_framework import serializers

from goods.models import GoodsCategory


class GoodsCategoryListSerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField()

    def get_parent_name(self, obj):
        parent = GoodsCategory.objects.filter(cat_id=obj.parent_id).first()
        if parent:
            return parent.cat_name
        return ''

    class Meta:
        model = GoodsCategory
        fields = ['cat_id', 'cat_name', 'keywords', 'cat_desc', 'parent_id', 'parent_name', 'sort_order', 'is_show',
                  'style_icon', 'cat_icon', 'pinyin_keyword', ]


class GoodsCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['cat_name', 'keywords', 'cat_desc', 'parent_id', 'sort_order', 'is_show']


class GoodsCategoryParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['cat_id', 'cat_name']


class GoodsCategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')
    id = serializers.SerializerMethodField('get_id')
    label = serializers.SerializerMethodField('get_name')

    def get_children(self, obj):
        children = GoodsCategory.objects.filter(parent_id=obj.cat_id).values(id=Lower('cat_id'),
                                                                             label=LTrim('cat_name')).all()
        return children

    def get_name(self, obj):
        return obj.cat_name

    def get_id(self, obj):
        return obj.cat_id

    class Meta:
        model = GoodsCategory
        fields = ['id', 'label', 'children']


class GoodsCategoryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['cat_name', 'keywords', 'cat_desc', 'parent_id', 'sort_order', 'is_show',
                  'pinyin_keyword', 'style_icon', 'cat_icon', ]
