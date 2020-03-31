from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import TemplateView
from rest_framework import generics

from order.filter.filters import OrderInfoFilter
from order.models import OrderInfo
from order.serializer.serializers import OrderInfoListSerializer
from system.pagination.paginator import CustomPagination


class OrderInfoListPageView(TemplateView):
    template_name = 'views/shop/order/list.html'


class OrderInfoListView(generics.ListAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoListSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = OrderInfoFilter


# class OrderInfoChangeView(generics.UpdateAPIView):
#     queryset = OrderInfo.objects.all()
#     serializer_class = OrderInfoUpdateSerializer
#
#
# class OrderInfoAddView(generics.CreateAPIView):
#     queryset = OrderInfo.objects.all()
#     serializer_class = OrderInfoAddSerializer
