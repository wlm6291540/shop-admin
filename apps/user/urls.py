from django.urls import path, re_path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from user.views import ShopUserListPageView, ShopUserListView, ShopUserChangeView, ShopUserChargeView, ShopUserAddView

user_urls = [
    path('user/list/view', ShopUserListPageView.as_view(), name='shop user view'),
    path('user/list/list', ShopUserListView.as_view(), name='shop user list'),
    path('user/list/add', ShopUserAddView.as_view(), name='shop user ladd'),
    path('user/list/update/<str:pk>', ShopUserChangeView.as_view(), name='shop user update'),
    path('user/list/charge/<str:pk>', ShopUserChargeView.as_view(), name='shop user charge'),
]
