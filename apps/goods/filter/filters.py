from django_filters import rest_framework as filters
import django_filters
from goods.models import GoodsBrand, GoodsCategory, Goods


class GoodsFilter(filters.FilterSet):
    """商品的过滤类"""
    # 区间查询,指定区间的最大最小值
    brand_name = django_filters.CharFilter(method='get_brand_name')
    cat_name = django_filters.CharFilter(method='get_cat_name')
    goods_name = filters.CharFilter(field_name='goods_name', lookup_expr='icontains')
    shop_price = filters.RangeFilter()
    platform = filters.CharFilter(field_name='platform', lookup_expr='icontains')
    country_name = filters.CharFilter(field_name='country_name', lookup_expr='icontains')
    pattern = filters.CharFilter(field_name='pattern', lookup_expr='pattern')
    lifes = filters.DateFromToRangeFilter()
    is_on_sale = filters.CharFilter(field_name='is_on_sale', lookup_expr='contains')
    is_delete = filters.CharFilter(field_name='is_delete', lookup_expr='contains')
    status = filters.CharFilter(field_name='status', lookup_expr='contains')
    create_time = filters.DateFromToRangeFilter()

    def get_brand_name(self, queryset, name, value):
        if value is not None or len(value) > 0:
            brand = GoodsBrand.objects.filter(brand_name__icontains=value).values_list('brand_id').all()
            if brand:
                return queryset.filter(brand_id__in=brand)
        return queryset

    def get_cat_name(self, queryset, name, value):
        if value is not None or len(value) > 0:
            cat = GoodsCategory.objects.filter(cat_name__icontains=value).values_list('cat_id').all()
            if cat:
                return queryset.filter(cat_id__in=cat)
        return queryset

    class Meta:
        model = Goods
        fields = ('goods_name', 'cat_name', 'brand_name', 'pattern', 'platform', 'lifes',
                  'country_name', 'is_on_sale', 'is_delete', 'status',)


class GoodsBrandFilter(filters.FilterSet):
    """品牌的过滤类"""
    # 区间查询,指定区间的最大最小值
    create_time = filters.DateFromToRangeFilter()
    brand_name = filters.CharFilter(field_name='brand_name', lookup_expr='icontains')
    brand_letter = filters.CharFilter(field_name='brand_letter', lookup_expr='icontains')
    is_show = filters.CharFilter(field_name='is_show', lookup_expr='contains')
    is_delete = filters.CharFilter(field_name='is_delete', lookup_expr='contains')
    status = filters.CharFilter(field_name='status', lookup_expr='contains')

    class Meta:
        model = GoodsBrand
        fields = ('create_time', 'brand_name', 'brand_letter', 'is_show', 'is_delete', 'status')


class GoodsCategoryFilter(filters.FilterSet):
    """分类的过滤类"""
    cat_name = filters.CharFilter(field_name='cat_name', lookup_expr='icontains')
    cat_desc = filters.CharFilter(field_name='cat_desc', lookup_expr='icontains')
    keywords = filters.CharFilter(field_name='keywords', lookup_expr='icontains')
    is_show = filters.CharFilter(field_name='is_show', lookup_expr='contains')

    class Meta:
        model = GoodsCategory
        fields = ['cat_name', 'keywords', 'is_show', 'cat_desc']
