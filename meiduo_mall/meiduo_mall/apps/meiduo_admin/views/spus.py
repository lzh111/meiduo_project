from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SPU, SPUSpecification, SpecificationOption, Brand
from meiduo_admin.serializers.spus import SPUSimpleSerializer, SPUSpecSerializer, SPUSpecificationSerializer, SPUSerializer, SPCEOptionSerializer, BrandSerializer



# GET /meiduo_admin/goods/simple/
class SPUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = SPU.objects.all()
    serializer_class = SPUSimpleSerializer

    # 关闭分页
    pagination_class = None


# GET /meiduo_admin/goods/(?P<pk>\d+)/specs/
class SPUSpecView(ListAPIView):
    permission_classes = [IsAdminUser]
    permission_classes = [IsAdminUser]

    serializer_class = SPUSpecSerializer
    # queryset = SPUSpecification.objects.filter(spu_id=pk)

    def get_queryset(self):
        """
        self.kwargs: 字典，保存从url地址中提取的所有命名参数
        """
        pk = self.kwargs['pk']
        return SPUSpecification.objects.filter(spu_id=pk)

    # 关闭分页
    pagination_class = None

    # def get(self, request):
    #     return self.list(request)

    # def get(self, request, pk):
    #     """
    #     获取SPU商品的规格选项数据:
    #     1. 查询获取SPU商品的规格数据
    #     2. 将SPU商品的规格数据序列化并返回
    #     """
    #     # 1. 查询获取SPU商品的规格数据
    #     specs = self.get_queryset()
    #
    #     # 2. 将SPU商品的规格数据序列化并返回
    #     serializer = self.get_serializer(specs, many=True)
    #     return Response(serializer.data)

# GET /meiduo_admin/goods/specs/
class SPUSpecsView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SPUSpecificationSerializer
    queryset = SPUSpecification.objects.all()
    # pagination_class = PageNum
    pagination_class = None


class SPUView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SPUSerializer
    queryset = SPU.objects.all()
    # pagination_class = PageNum
    pagination_class = None


class SPCEOptionView(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SpecificationOption.objects.all()
    serializer_class = SPCEOptionSerializer
    # pagination_class = PageNum
    pagination_class = None

class GoodsBrandsView(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # pagination_class = PageNum
    pagination_class = None





class SPUSimpleView(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SPUSerializer
    def get_queryset(self):
        """
        self.kwargs: 字典，保存从url地址中提取的所有命名参数
        """
        pk = self.kwargs['pk']
        return SPU.objects.filter(id=pk)
    # pagination_class = PageNum
    pagination_class = None

class SPUGoodsView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = SPU.objects.all()
    serializer_class = SPUSimpleSerializer
    # pagination_class = PageNum
    pagination_class = None

class SPUGoodsSpecView(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecSerializer
    # pagination_class = PageNum
    pagination_class = None