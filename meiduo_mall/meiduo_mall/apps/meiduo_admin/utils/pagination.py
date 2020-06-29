from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


# page=<页码>&pagesize=<页容量>
class StandardResultPagination(PageNumberPagination):
    # 分页时默认页容量
    page_size = 5
    # 获取分页数据时，传递页容量参数的名称
    page_size_query_param = 'pagesize'
    # 分页时的最大页容量
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('counts', self.page.paginator.count),
            ('lists', data),
            ('page', self.page.number),
            ('pages', self.page.paginator.num_pages),
            ('pagesize', self.get_page_size(self.request))
        ]))