from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets, mixins, generics, pagination, status
from rest_framework.response import Response

from system.models import Menu
from system.pagination.paginator import CustomPagination
from system.serializers.serializers_menu import MenuSerializer, MenuTreeSerializer


class MenuPageView(TemplateView):
    template_name = 'views/user/menu/list.html'


class MenuAddView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuChangeView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDeleteView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        if title is not None:
            self.queryset = self.queryset.filter(title=title)
        return self.queryset


class MenuTreeViewSet(viewsets.ViewSet):
    """
    菜单树列表
    """
    def list(self, request):
        queryset = Menu.objects.filter(parent=None).all()
        serializer = MenuTreeSerializer(queryset, many=True)
        return Response(serializer.data)
