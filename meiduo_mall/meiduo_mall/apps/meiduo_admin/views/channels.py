from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory
from meiduo_admin.serializers.channels import ChannelSerializer, ChannelTypeSerializer, ChannelCategorySerializer


class ChannelViewSet(ModelViewSet):
    """频道管理的视图集"""
    permission_classes = [IsAdminUser]
    # 指定视图所使用的查询集
    queryset = GoodsChannel.objects.all()
    # 指定视图所使用的序列化器类
    serializer_class = ChannelSerializer

    # GET /meiduo_admin/goods/channels/ -> list
    # POST /meiduo_admin/goods/channels/ -> create
    # GET /meiduo_admin/goods/channels/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/goods/channels/(?P<pk>\d+)/ -> update
    # DELETE /meiduo_admin/goods/channels/(?P<pk>\d+)/ -> destroy

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save() # 调用序列化器类中的create
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save() # 调用序列化器类中的update
    #     return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# GET /meiduo_admin/goods/channel_types/
class ChannelTypesView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = GoodsChannelGroup.objects.all()
    serializer_class = ChannelTypeSerializer


    # 关闭分页
    pagination_class = None

    # def get(self, request):
    #     return self.list(request)

    # def get(self, request):
    #     """
    #     获取所有频道组的数据:
    #     1. 查询获取所有的频道组数据
    #     2. 将频道组的数据序列化并返回
    #     """
    #     # 1. 查询获取所有的频道组数据
    #     groups = self.get_queryset()
    #
    #     # 2. 将频道组的数据序列化并返回
    #     serializer = self.get_serializer(groups, many=True)
    #     return Response(serializer.data)


# GET /meiduo_admin/goods/categories/
class ChannelCategoriesView(ListAPIView):
    permission_classes = [IsAdminUser]

    serializer_class = ChannelCategorySerializer
    queryset = GoodsCategory.objects.filter(parent=None)

    # 关闭分页
    pagination_class = None


class ChannelsView(ListAPIView):
    permission_classes = [IsAdminUser]

    serializer_class = ChannelSerializer
    queryset = GoodsChannel.objects.all()
    # 关闭分页
    pagination_class = None

class Channel(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ChannelCategorySerializer

    def get_queryset(self):
        """
        self.kwargs: 字典，保存从url地址中提取的所有命名参数
        """
        pk = self.kwargs['pk']
        return GoodsCategory.objects.filter(parent_id=pk)
    # 关闭分页
    pagination_class = None