from django_filters import rest_framework as filters

from goods.models import GoodsBrand


class GoodsBrandFilter(filters.FilterSet):
    """品牌的过滤类"""
    # 区间查询,指定区间的最大最小值
    create_time = filters.DateFromToRangeFilter()

    class Meta:
        model = GoodsBrand
        fields = ('create_time', 'brand_name', 'brand_letter', 'is_show', 'is_delete', 'status')
