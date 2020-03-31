from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsBrand
from user.models import Users


class GoodsListSerializer(serializers.ModelSerializer):
    cat_name = serializers.SerializerMethodField()
    brand_name = serializers.SerializerMethodField()

    def get_cat_name(self, obj):
        try:
            cat = GoodsCategory.objects.get(cat_id=obj.cat_id)
            return cat.cat_name
        except Exception:
            return None

    def get_brand_name(self, obj):
        try:
            brand = GoodsBrand.objects.get(brand_id=obj.brand_id)
            return brand.brand_name
        except Exception as e:
            return None



    class Meta:
        model = Goods
        fields = ['goods_id', 'cat_id', 'cat_name', 'goods_sn', 'bar_code', 'goods_name', 'brand_id', 'brand_name',
                  'goods_number', 'is_freepost', 'cost_price', 'shop_price', 'warn_number', 'desc_mobile',
                  'goods_thumb', 'is_on_sale', 'is_delete', 'status', 'pinyin_keyword', 'goods_unit', 'pattern',
                  'platform', 'source_code', 'lifes', 'country_name', 'create_time']
