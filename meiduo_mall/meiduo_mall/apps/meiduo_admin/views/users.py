from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from meiduo_admin.serializers.users import AdminAuthSerializer, UserInfoSerializer

from users.models import User


# POST /meiduo_admin/authorizations/
class AdminAuthView(CreateAPIView):
    # 指定视图所使用的序列化器类
    serializer_class = AdminAuthSerializer

    # def post(self, request):
    #     return self.create(request)

    # def post(self, request):
    #     """
    #     管理员登录:
    #     1. 获取参数并进行校验(参数完整性，用户名和密码是否正确)
    #     2. 创建jwt token保存登录用户的身份信息
    #     3. 返回响应的数据
    #     """
    #     # 1. 获取参数并进行校验(参数完整性，用户名和密码是否正确)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # 2. 创建jwt token保存登录用户的身份信息
    #     serializer.save() # 调用序列化器类create
    #
    #     # 3. 返回响应的数据
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# GET /meiduo_admin/users/?keyword=<关键字>
class UserInfoView(ListCreateAPIView):
    permission_classes = [IsAdminUser]

    serializer_class = UserInfoSerializer
    # queryset = None

    def get_queryset(self):
        """
        self.request: 请求对象
        """
        keyword = self.request.query_params.get('keyword')

        if keyword:
            # 1.1 如果传递了keyword，根据用户名查询用户名含有keyword的普通用户
            users = User.objects.filter(username__contains=keyword, is_staff=False)
        else:
            # 1.2 如果未传递keyword，查询所有的普通用户
            users = User.objects.filter(is_staff=False)

        return users

    @method_decorator(permission_required('users.view_user_api', raise_exception=True))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # def get(self, request):
    #     return self.list(request)

    # def get(self, request):
    #     """
    #     获取网站的普通用户的数据:
    #     1. 查询获取普通用户的数据
    #         1.1 如果传递了keyword，根据用户名查询用户名含有keyword的普通用户
    #         1.2 如果未传递keyword，查询所有的普通用户
    #     2. 将普通用户的数据序列化并返回
    #     """
    #     # 1. 查询获取普通用户的数据
    #     users = self.get_queryset()
    #
    #     # 2. 将普通用户的数据序列化并返回
    #     serializer = self.get_serializer(users, many=True)
    #     return Response(serializer.data)

    # POST /meiduo_admin/users/
    # def post(self, request):
    #     """
    #     保存新增用户的数据:
    #     1. 获取参数并进行校验（参数完整性、用户名是否已注册、手机号格式、手机号是否注册、邮箱格式）
    #     2. 保存新增用户的数据
    #     3. 将新增用户的数据序列化并返回
    #     """
    #     # 1. 获取参数并进行校验（参数完整性、用户名是否已注册、手机号格式、手机号是否注册、邮箱格式）
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # 2. 保存新增用户的数据
    #     serializer.save() # 调用序列化器类的create
    #
    #     # 3. 将新增用户的数据序列化并返回
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def post(self, request):
    #     return self.create(request)
