from django.conf.urls import url, include
from django.urls import path, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from system.views.views import MainPageView, ConsolePageView, ImageUploadView
from system.views.views_menu import (MenuPageView, MenuTreeViewSet, MenuListView, MenuAddView, MenuDeleteView,
                                     MenuChangeView)
from system.views.views_permission import PermPageView
from system.views.views_role import (RolePageView, RoleListView, RoleAddView, RoleDeleteView, RoleChangeView,
                                     RoleBindView, RoleUserView, RoleMenuView, RoleMenuBindView)
from system.views.views_user import (LoginView, UserPageView, UserListView, UserAddView, UserChangeView,
                                     UserActiveView, LogoutView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


system_urls = [
    path('',  MainPageView.as_view(), name='main page'),
    path('login', LoginView.as_view(), name='login page and view'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('main/view', MainPageView.as_view(), name='main page'),
    path('main/console/view', ConsolePageView.as_view(), name='console page'),

    # 图片上传
    path('upload', ImageUploadView.as_view(), name='image upload view'),

    # menu
    path('system/menu/view', MenuPageView.as_view(), name='menu page'),
    path('system/menu/tree', MenuTreeViewSet.as_view({'get': 'list'}), name='menu tree'),
    path('system/menu/list', MenuListView.as_view(), name='menu list'),
    path('system/menu/add', MenuAddView.as_view(), name='menu add'),
    path('system/menu/delete/<int:pk>', MenuDeleteView.as_view(), name='menu delete'),
    path('system/menu/update/<int:pk>', MenuChangeView.as_view(), name='menu update'),

    # role
    path('system/role/view', RolePageView.as_view(), name='role page'),
    path('system/role/list', RoleListView.as_view(), name='role list'),
    path('system/role/add', RoleAddView.as_view(), name='role add'),
    path('system/role/delete/<int:pk>', RoleDeleteView.as_view(), name='role delete'),
    path('system/role/update/<int:pk>', RoleChangeView.as_view(), name='role update'),
    path('system/role/role_user/<int:pk>', RoleUserView.as_view(), name='role user'),
    path('system/role/role_user/bind/<int:pk>', RoleBindView.as_view(), name='role bind'),
    path('system/role/role_menu/<int:pk>', RoleMenuView.as_view(), name='role menu'),
    path('system/role/role_menu/bind/<int:pk>', RoleMenuBindView.as_view(), name='role menu'),

    # user
    path('system/user/view', UserPageView.as_view(), name='user page'),
    path('system/user/list', UserListView.as_view(), name='user list'),
    path('system/user/add', UserAddView.as_view(), name='user add'),
    # path('system/menu/delete/<int:pk>', MenuDeleteView.as_view(), name='menu delete'),
    path('system/user/update/<int:pk>', UserChangeView.as_view(), name='user update'),
    path('system/user/active/<int:pk>', UserActiveView.as_view(), name='user active'),

]
