from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from users.models import User
from meiduo_admin.serializers.permissions import PermissionSerializer, ContentTypeSerializer, GroupSerializer, \
    PermSimpleSerializer, AdminSerializer, GroupSimpleSerializer


class PermissionViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    # GET /meiduo_admin/permission/perms/ -> list
    # POST /meiduo_admin/permission/perms/ -> create
    # GET /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> update
    # DELETE /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> destroy
    # GET /meiduo_admin/permission/content_types/ -> content_types

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save() # 调用序列化器类中的create
    #     return Response(serializer.data, status=201)

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
    #     return Response(status=204)

    def content_types(self, request):
        """
        获取权限内容类型的数据:
        1. 查询获取所有权限内容类型的数据
        2. 将权限内容类型数据序列化并返回
        """
        # 1. 查询获取所有权限内容类型的数据
        c_types = ContentType.objects.all()

        # 2. 将权限内容类型数据序列化并返回
        serializer = ContentTypeSerializer(c_types, many=True)
        return Response(serializer.data)


class GroupViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # GET /meiduo_admin/permission/groups/ -> list
    # POST /meiduo_admin/permission/groups/ -> create
    # GET /meiduo_admin/permission/groups/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/permission/groups/(?P<pk>\d+)/ -> update
    # DELETE /meiduo_admin/permission/groups/(?P<pk>\d+)/ -> destroy
    # GET /meiduo_admin/permission/simple/ -> simple

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save() # 调用序列化器类中的create
    #     return Response(serializer.data, status=201)

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
    #     return Response(status=204)

    def simple(self, request):
        """
        获取权限的简单数据:
        1. 查询获取所有的权限数据
        2. 将权限数据序列化并返回
        """
        # 1. 查询获取所有的权限数据
        perms = Permission.objects.all()

        # 2. 将权限数据序列化并返回
        serializer = PermSimpleSerializer(perms, many=True)
        return Response(serializer.data)


class AdminViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer

    # GET /meiduo_admin/permission/admins/ -> list
    # POST /meiduo_admin/permission/admins/ -> create
    # GET /meiduo_admin/permission/admins/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/permission/admins/(?P<pk>\d+)/ -> update
    # DELETE /meiduo_admin/permission/admins/(?P<pk>\d+)/ -> destroy
    # GET /meiduo_admin/permission/groups/simple/ -> simple

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save() # 调用序列化器类中的create
    #     return Response(serializer.data, status=201)

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
    #     return Response(status=204)

    def simple(self, request):
        """
        获取用户组的简单数据:
        1. 查询获取所有用户组的数据
        2. 将用户组数据序列化并返回
        """
        # 1. 查询获取所有用户组的数据
        groups = Group.objects.all()

        # 2. 将用户组数据序列化并返回
        serializer = GroupSimpleSerializer(groups, many=True)
        return Response(serializer.data)
