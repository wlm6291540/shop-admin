from django.urls import path, re_path

from goods.views import GoodsListPageView, GoodsListView
from goods.views_brand import (GoodBrandAddView, GoodBrandListPageView, GoodBrandListView,
                               GoodBrandChangeView, GoodBrandBatchDeleteView)
from goods.views_category import GoodsCategoryPageView, GoodsCategoryListView

goods_urls = [
    # goods
    path('goods/list/view', GoodsListPageView.as_view(), name='goods view'),
    path('goods/list/list', GoodsListView.as_view(), name='good list'),
    # path('goods/brand/add', GoodBrandAddView.as_view(), name='good brand add'),
    # path('goods/brand/update/<str:pk>', GoodBrandChangeView.as_view(), name='good brand update'),
    # path('goods/brand/delete', GoodBrandBatchDeleteView.as_view(), name='good brand batch delete'),

    # category
    path('goods/category/view', GoodsCategoryPageView.as_view(), name='good category view'),
    path('goods/category/list', GoodsCategoryListView.as_view(), name='good category list'),
    # path('goods/brand/add', GoodBrandAddView.as_view(), name='good brand add'),
    # path('goods/brand/update/<str:pk>', GoodBrandChangeView.as_view(), name='good brand update'),
    # path('goods/brand/delete', GoodBrandBatchDeleteView.as_view(), name='good brand batch delete'),

    # brand
    path('goods/brand/view', GoodBrandListPageView.as_view(), name='good brand view'),
    path('goods/brand/list', GoodBrandListView.as_view(), name='good brand list'),
    path('goods/brand/add', GoodBrandAddView.as_view(), name='good brand add'),
    path('goods/brand/update/<str:pk>', GoodBrandChangeView.as_view(), name='good brand update'),
    path('goods/brand/delete', GoodBrandBatchDeleteView.as_view(), name='good brand batch delete'),
]
