import json

from django.http import JsonResponse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response

from goods.filter.filters import GoodsCategoryFilter
from goods.models import GoodsCategory
from goods.serializer.serializers_category import GoodsCategoryListSerializer
from system.pagination.paginator import CustomPagination
from goods.serializer.serializers_brand import *


class GoodsCategoryPageView(TemplateView):
    template_name = 'views/shop/category/list.html'


class GoodsCategoryListView(generics.ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategoryListSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsCategoryFilter


# class GoodsCategoryChangeView(generics.UpdateAPIView):
#     queryset = GoodsCategory.objects.all()
#     serializer_class = GoodsCategoryUpdateSerializer
#
#
# class GoodsCategoryAddView(generics.CreateAPIView):
#     queryset = GoodsCategory.objects.all()
#     serializer_class = GoodsCategoryAddSerializer
