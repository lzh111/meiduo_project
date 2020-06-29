from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAdminUser

from django.db.models import Q

from meiduo_admin.serializers.orders import OrderListSerializer, OrderDetailSerializer, OrderStatusSerializer, OrderSeriazlier
from orders.models import OrderInfo


class OrdersViewSet(UpdateModelMixin, ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]

    # queryset = None

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')

        if keyword:
            # order.skus.all()[0].sku.name
            # 查询条件：订单id等于keyword 或者 和订单关联的订单商品对应的sku商品的名称中含有keyword
            orders = OrderInfo.objects.filter(Q(order_id=keyword) |
                                              Q(skus__sku__name__contains=keyword)).distinct()
        else:
            # 获取所有订单的信息
            orders = OrderInfo.objects.all()

        return orders

    # serializer_class = OrderListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        elif self.action == 'retrieve':
            return OrderDetailSerializer
        else:
            # status
            return OrderStatusSerializer

    # GET /meiduo_admin/orders/ -> list
    # GET /meiduo_admin/orders/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/orders/(?P<pk>\d+)/status/ -> status

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def status(self, request):
        return self.update(request)

    # @action(methods=['put'], detail=True)
    # def status(self, request, pk):
    #     """
    #     修改指定订单的状态:
    #     1. 根据pk获取指定的订单
    #     2. 获取status并进行校验(status是否传递，status是否合法)
    #     3. 修改指定订单的状态
    #     4. 返回响应
    #     """
    #     # 1. 根据pk获取指定的订单
    #     order = self.get_object()
    #
    #     # 2. 获取status并进行校验(status是否传递，status是否合法)
    #     serializer = self.get_serializer(order, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # 3. 修改指定订单的状态
    #     serializer.save()
    #
    #     # 4. 返回响应
    #     return Response(serializer.data)

class OrdersView(ModelViewSet):
    serializer_class = OrderSeriazlier
    queryset = OrderInfo.objects.all()
    pagination_class = None