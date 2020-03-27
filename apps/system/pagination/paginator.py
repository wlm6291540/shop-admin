from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('code', 0),
            ('msg', '获取成功'),
            ('count', self.page.paginator.count),
            ('data', data)
        ]))