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
