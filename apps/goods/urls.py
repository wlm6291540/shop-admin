from django.urls import path, re_path

from goods.views_brand import (GoodBrandAddView, GoodBrandListPageView, GoodBrandListView,
                               GoodBrandChangeView, GoodBrandBatchDeleteView)

goods_urls = [
    # brand
    path('goods/brand/view', GoodBrandListPageView.as_view(), name='good brand view'),
    path('goods/brand/list', GoodBrandListView.as_view(), name='good brand list'),
    path('goods/brand/add', GoodBrandAddView.as_view(), name='good brand add'),
    path('goods/brand/update/<str:pk>', GoodBrandChangeView.as_view(), name='good brand update'),
    path('goods/brand/delete', GoodBrandBatchDeleteView.as_view(), name='good brand batch delete'),
]
