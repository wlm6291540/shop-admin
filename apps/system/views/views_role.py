import json

from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets, mixins, generics, pagination, status
from rest_framework.response import Response

from system.models import Role, User, Menu
from system.pagination.paginator import CustomPagination
from system.serializers.serializers_menu import MenuTreeSerializer
from system.serializers.serializers_role import RoleSerializer, RoleUserSerializer, RoleBindSerializer, \
    RoleMenuBindSerializer, RoleMenuSerializer


class RolePageView(TemplateView):
    template_name = 'views/user/role/list.html'


class RoleAddView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleChangeView(generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDeleteView(generics.DestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'pk'


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        if title is not None:
            self.queryset = self.queryset.filter(title=title)
        return self.queryset


class RoleUserView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleUserSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            self.queryset = self.queryset.filter(name=name)
        return self.queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if False:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        role_users = self.get_object().users.all()
        all_users = User.objects.all()
        binds = []
        for user in role_users:
            binds.append(user.id)
        all_users = self.get_serializer(all_users, many=True).data
        ret = dict(code=1, msg='获取成功', data={'binds': binds, 'all': all_users})
        return Response(ret)


class RoleBindView(generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleBindSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        ids = request.data.get('users', None)
        ids = json.loads(ids)
        users = User.objects.filter(id__in=ids)
        instance = self.get_object()
        instance.users.set(users)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class RoleMenuView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleMenuSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            self.queryset = self.queryset.filter(name=name)
        return self.queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if False:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        role_menus = self.get_object().menus.all()
        all_menus = Menu.objects.all()
        serializer = self.get_serializer(all_menus, many=True, role_menus=role_menus)
        data = self.to_tree(serializer.data)
        return Response(data)

    def to_tree(self, data):
        top_menu = list(filter(lambda x: x.get('parent') is None, data))
        for menu in top_menu:
            menu['children'] = list(filter(lambda x: x.get('parent') == menu.get('id'), data))
            for second_menu in menu['children']:
                second_menu['children'] = list(filter(lambda x: x.get('parent') == second_menu.get('id'), data))
                for third_menu in second_menu['children']:
                    third_menu['children'] = list(filter(lambda x: x.get('parent') == third_menu.get('id'), data))
        return top_menu


class RoleMenuBindView(generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleMenuBindSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        menus = request.data.get('menus', None)
        if menus:
            menus = json.loads(menus)
            ids = self.get_ids(menus)
            menus = Menu.objects.filter(id__in=ids)
            instance = self.get_object()
            instance.menus.set(menus)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        else:
            raise Exception('参数错误')
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get_ids(self, menus):
        ids = []
        for menu in menus:
            ids.append(menu.get('id'))
            children = menu.get('children')
            if children:
                ids.extend(self.get_ids(children))
        return ids
