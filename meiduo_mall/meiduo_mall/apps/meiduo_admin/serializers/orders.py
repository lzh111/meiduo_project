from rest_framework import serializers

from goods.models import SKU
from orders.models import OrderInfo, OrderGoods


class OrderListSerializer(serializers.ModelSerializer):
    """订单序列化器类"""
    create_time = serializers.DateTimeField(label='创建时间', format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = OrderInfo
        fields = ('order_id', 'create_time')


class OrderSKUSerializer(serializers.ModelSerializer):
    """SKU商品序列化器类"""
    class Meta:
        model = SKU
        fields = ('id', 'name', 'default_image')


class OrderGoodsSerializer(serializers.ModelSerializer):
    """订单商品序列化器类"""
    sku = OrderSKUSerializer(label='SKU商品')

    class Meta:
        model = OrderGoods
        fields = ('id', 'count', 'price', 'sku')


class OrderDetailSerializer(serializers.ModelSerializer):
    """订单序列化器类"""
    skus = OrderGoodsSerializer(label='订单商品', many=True)

    user = serializers.StringRelatedField(label='用户')

    create_time = serializers.DateTimeField(label='下单时间', format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = OrderInfo
        exclude = ('update_time', 'address')


class OrderStatusSerializer(serializers.ModelSerializer):
    """订单序列化器类"""
    class Meta:
        model = OrderInfo
        fields = ('status', 'order_id')
        read_only_fields = ('order_id', )

        # extra_kwargs = {
        #     'order_id': {
        #         'read_only': True
        #     }
        # }
class OrderSeriazlier(serializers.ModelSerializer):

    class Meta:
        model =  OrderInfo
        fields = '__all__'