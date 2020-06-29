from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from users.models import User


class PermissionSerializer(serializers.ModelSerializer):
    """权限序列化器类"""
    class Meta:
        model = Permission
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    """权限内容类型序列化器类"""
    class Meta:
        model = ContentType
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    """用户组序列化器类"""
    class Meta:
        model = Group
        fields = '__all__'


class PermSimpleSerializer(serializers.ModelSerializer):
    """权限序列化器类"""
    class Meta:
        model = Permission
        fields = ('id', 'name')


class AdminSerializer(serializers.ModelSerializer):
    """管理员用户序列化器类"""
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'groups', 'user_permissions', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': False,
                'allow_blank': True
            }
        }

    def create(self, validated_data):
        validated_data['is_staff'] = True

        # 添加管理员用户
        admin = super().create(validated_data)

        # 设置密码
        password = validated_data.get('password')

        if not password:
            # 默认密码
            password = '123456abc'

        admin.set_password(password)
        admin.save()

        return admin

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        # 修改管理员数据
        super().update(instance, validated_data)

        # 修改密码
        if password:
            instance.set_password(password)
            instance.save()

        return instance


class GroupSimpleSerializer(serializers.ModelSerializer):
    """用户组序列化器类"""
    class Meta:
        model = Group
        fields = ('id', 'name')
