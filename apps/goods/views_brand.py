import json

from django.http import JsonResponse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response

from goods.filter.filters import GoodsBrandFilter
from system.pagination.paginator import CustomPagination
from goods.serializer.serializers_brand import *


class GoodBrandListPageView(TemplateView):
    template_name = 'views/shop/brand/list.html'


class GoodBrandListView(generics.ListAPIView):
    queryset = GoodsBrand.objects.all()
    serializer_class = GoodsBrandListSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsBrandFilter


class GoodBrandChangeView(generics.UpdateAPIView):
    queryset = GoodsBrand.objects.all()
    serializer_class = GoodsBrandUpdateSerializer


class GoodBrandAddView(generics.CreateAPIView):
    queryset = GoodsBrand.objects.all()
    serializer_class = GoodsBrandAddSerializer


class GoodBrandBatchDeleteView(View):
    def post(self, request):
        code = 0
        msg = '删除成功'
        ids = request.POST.get('ids', None)
        if ids:
            ids = json.loads(ids)
            goodsBrand = GoodsBrand.objects.filter(brand_id__in=ids)
            goodsBrand.delete()
        else:
            code = 1
            msg = '删除失败'
        ret = dict(code=code, msg=msg)
        return JsonResponse(ret)
