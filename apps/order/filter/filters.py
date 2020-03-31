from django_filters import rest_framework
import django_filters
from order.models import OrderInfo
from goods.models import Goods
from user.models import Users


class OrderInfoFilter(rest_framework.FilterSet):
    order_status = django_filters.CharFilter(field_name='order_status', lookup_expr='contains')
    create_time = django_filters.DateFromToRangeFilter()
    pay_time = django_filters.DateFromToRangeFilter()
    user_name = django_filters.CharFilter(method='get_user_name')
    goods_name = django_filters.CharFilter(method='get_goods_name')

    def get_goods_name(self, queryset, name, value):
        if value is not None or len(value) > 0:
            goods = Goods.objects.filter(goods_name__icontains=value).values_list('goods_id').all()
            if goods:
                return queryset.filter(goods_id__in=goods)
        return queryset

    def get_user_name(self, queryset, name, value):
        if value is not None or len(value) > 0:
            users = Users.objects.filter(user_name__icontains=value).values_list('user_id').all()
            if users:
                return queryset.filter(user_id__in=users)
        return queryset

    class Meta:
        model = OrderInfo
        fields = ['goods_name', 'user_name', 'create_time', 'pay_time', 'order_status']
