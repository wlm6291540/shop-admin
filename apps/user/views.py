import time
import uuid

from django_filters.rest_framework import DjangoFilterBackend

from user.filter.filters import UsersFilter
from utils.util import make_password

# Create your views here.
from django.views import View
from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response

from system.pagination.paginator import CustomPagination
from user.models import Users
from user.serializer.serializers import *
from utils.RSA import RSA


class ShopUserListPageView(TemplateView):
    template_name = 'views/shop/user/list.html'


class ShopUserListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = ShopUserListSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = UsersFilter


class ShopUserChangeView(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = ShopUserUpdateSerializer


class ShopUserChargeView(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = ShopUserChargeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        balance = instance.user_money
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user_money'] += balance
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ShopUserAddView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = ShopUserAddSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        name = serializer.validated_data['user_name']
        serializer.validated_data['user_id'] = uuid.uuid3(uuid.NAMESPACE_DNS, name)
        serializer.validated_data['reg_time'] = int(time.time())
        serializer.validated_data['private_key'] = RSA().get_private_key()
        serializer.validated_data['public_key'] = RSA().get_public_key()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
