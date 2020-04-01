from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import TemplateView
from rest_framework import generics

from goods.filter.filters import GoodsFilter
from goods.models import GoodsCategory, Goods
from goods.serializer.serializers_goods import GoodsListSerializer, GoodsUpdateSerializer, GoodsOnSaleSerializer, \
    GoodsPriceUpdateSerializer
from system.pagination.paginator import CustomPagination


class GoodsListPageView(TemplateView):
    template_name = 'views/shop/goods/list.html'


class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsListSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsFilter


class GoodsOnSaleView(generics.UpdateAPIView):
    queryset = Goods
    serializer_class = GoodsOnSaleSerializer


class GoodsChangeView(generics.UpdateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsUpdateSerializer


class GoodsPriceChangeView(generics.UpdateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsPriceUpdateSerializer
