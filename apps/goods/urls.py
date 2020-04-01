from django.urls import path, re_path

from goods.views import GoodsListPageView, GoodsListView, GoodsOnSaleView, GoodsChangeView, GoodsPriceChangeView
from goods.views_brand import (GoodBrandAddView, GoodBrandListPageView, GoodBrandListView,
                               GoodBrandChangeView, GoodBrandBatchDeleteView, GoodBrandAllListView)
from goods.views_category import GoodsCategoryPageView, GoodsCategoryListView, GoodsCategoryTreeView, \
    GoodsCategoryChangeView, GoodsCategoryAddView, GoodsCategoryBatchDeleteView, GoodsCategoryParentView

goods_urls = [
    # goods
    path('goods/list/view', GoodsListPageView.as_view(), name='goods view'),
    path('goods/list/list', GoodsListView.as_view(), name='good list'),
    path('goods/list/on_sale/<str:pk>', GoodsOnSaleView.as_view(), name='good on sale'),
    path('goods/list/update/<str:pk>', GoodsChangeView.as_view(), name='good update'),
    path('goods/list/price_update/<str:pk>', GoodsPriceChangeView.as_view(), name='good price update'),
    # path('goods/brand/delete', GoodBrandBatchDeleteView.as_view(), name='good brand batch delete'),

    # category
    path('goods/category/view', GoodsCategoryPageView.as_view(), name='good category view'),
    path('goods/category/list', GoodsCategoryListView.as_view(), name='good category list'),
    path('goods/category/add', GoodsCategoryAddView.as_view(), name='good category add'),
    path('goods/category/update/<str:pk>', GoodsCategoryChangeView.as_view(), name='good category update'),
    path('goods/category/delete', GoodsCategoryBatchDeleteView.as_view(), name='good category batch delete'),
    path('goods/category/parent', GoodsCategoryParentView.as_view(), name='good category parent'),
    path('goods/category/tree', GoodsCategoryTreeView.as_view(), name='good category tree'),

    # brand
    path('goods/brand/view', GoodBrandListPageView.as_view(), name='good brand view'),
    path('goods/brand/list', GoodBrandListView.as_view(), name='good brand list'),
    path('goods/brand/all_list', GoodBrandAllListView.as_view(), name='good brand all list'),
    path('goods/brand/add', GoodBrandAddView.as_view(), name='good brand add'),
    path('goods/brand/update/<str:pk>', GoodBrandChangeView.as_view(), name='good brand update'),
    path('goods/brand/delete', GoodBrandBatchDeleteView.as_view(), name='good brand batch delete'),
]
