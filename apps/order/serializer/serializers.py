from rest_framework import serializers

from goods.models import Goods
from order.models import OrderInfo
from user.models import Users


class OrderInfoListSerializer(serializers.ModelSerializer):
    order_status_name = serializers.SerializerMethodField()
    goods_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()

    def get_order_status_name(self, obj):
        return obj.get_order_status_display()

    def get_goods_name(self, obj):
        try:
            goods = Goods.objects.get(goods_id=obj.goods_id)
            return goods.goods_name
        except Exception as e:
            return None

    def get_user_name(self, obj):
        try:
            user = Users.objects.get(user_id=obj.user_id)
            return user.user_name
        except Exception as e:
            return None

    def get_company_name(self, obj):
        try:
            user = Users.objects.get(user_id=obj.user_id)
            return user.company_name
        except Exception as e:
            return None

    class Meta:
        model = OrderInfo
        fields = ['order_sn', 'user_id', 'order_status', 'order_status_name', 'consignee', 'province', 'city',
                  'district', 'address', 'mobile', 'order_amount', 'create_time', 'pay_time', 'ship_code', 'ship_name',
                  'shipping_no', 'froms', 'rel_name', 'id_num', 'goods_id', 'goods_name', 'goods_sn', 'num',
                  'product_num', 'life', 'remark', 'shipping_fee', 'user_name', 'company_name']
