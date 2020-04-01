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
from goods.serializer.serializers_category import GoodsCategoryListSerializer, GoodsCategoryTreeSerializer, \
    GoodsCategoryUpdateSerializer, GoodsCategoryAddSerializer, GoodsCategoryParentSerializer
from system.pagination.paginator import CustomPagination


class GoodsCategoryPageView(TemplateView):
    template_name = 'views/shop/category/list.html'


class GoodsCategoryListView(generics.ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategoryListSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsCategoryFilter


class GoodsCategoryChangeView(generics.UpdateAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategoryUpdateSerializer


class GoodsCategoryAddView(generics.CreateAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategoryAddSerializer


class GoodsCategoryParentView(generics.ListAPIView):
    queryset = GoodsCategory.objects.filter(parent_id=0).all()
    serializer_class = GoodsCategoryParentSerializer


class GoodsCategoryTreeView(generics.ListAPIView):
    queryset = GoodsCategory.objects.filter(parent_id=0).all()
    serializer_class = GoodsCategoryTreeSerializer
    pagination_class = None


class GoodsCategoryBatchDeleteView(View):
    def post(self, request):
        code = 0
        msg = '删除成功'
        ids = request.POST.get('ids', None)
        if ids:
            ids = json.loads(ids)
            cats = GoodsCategory.objects.filter(cat_id__in=ids)
            cats.delete()
        else:
            code = 1
            msg = '删除失败'
        ret = dict(code=code, msg=msg)
        return JsonResponse(ret)