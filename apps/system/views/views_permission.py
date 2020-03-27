from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets, mixins, generics, pagination, status
from rest_framework.response import Response

from system.models import Menu
from system.pagination.paginator import CustomPagination
from system.serializers.serializers_menu import MenuSerializer, MenuTreeSerializer


class PermPageView(TemplateView):
    template_name = 'views/user/perm/list.html'
