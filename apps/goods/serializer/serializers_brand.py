import time

from rest_framework import serializers

from goods.models import GoodsBrand
from user.models import Users


class GoodsBrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBrand
        fields = ['brand_id', 'brand_name', 'brand_letter', 'brand_first_char', 'brand_logo', 'index_img', 'brand_bg',
                  'brand_desc', 'site_url', 'sort_order', 'is_show', 'is_delete', 'status', 'create_time',
                  'name_pinyin']


class GoodsBrandAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBrand
        fields = ['brand_name', 'brand_letter', 'brand_first_char', 'brand_logo', 'index_img', 'brand_bg',
                  'brand_desc', 'site_url', 'sort_order', 'is_show', 'is_delete', 'status', 'create_time',
                  'name_pinyin']


class GoodsBrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBrand
        fields = ['brand_id', 'brand_name', 'brand_letter', 'brand_first_char', 'brand_logo', 'index_img', 'brand_bg',
                  'brand_desc', 'site_url', 'sort_order', 'is_show', 'is_delete', 'status', 'create_time',
                  'name_pinyin']


class GoodsBrandChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBrand
        fields = ['user_money']
