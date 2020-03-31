from django.urls import path, re_path

from order.views import (OrderInfoListPageView, OrderInfoListView)

order_urls = [
    # order
    path('order/list/view', OrderInfoListPageView.as_view(), name='order view'),
    path('order/list/list', OrderInfoListView.as_view(), name='order list'),
    # path('goods/brand/add', GoodBrandAddView.as_view(), name='good brand add'),
    # path('goods/brand/update/<str:pk>', GoodBrandChangeView.as_view(), name='good brand update'),
    # path('goods/brand/delete', GoodBrandBatchDeleteView.as_view(), name='good brand batch delete'),
]
