from rest_framework import serializers

from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory, GoodsChannelGroup


# channel.group: 和频道关联的频道组的对象
# channel.category: 和频道关联的一级分类的对象
class ChannelSerializer(serializers.ModelSerializer):
    """频道的序列化器类"""
    group_id = serializers.IntegerField(label='频道组的id')
    category_id = serializers.IntegerField(label='一级分类id')

    # 关联对象的嵌套序列化
    group = serializers.StringRelatedField(label='频道组')
    category = serializers.StringRelatedField(label='一级分类')

    class Meta:
        model = GoodsChannel
        exclude = ('create_time', 'update_time')

    def validate_group_id(self, value):
        # 校验频道组是否存在
        try:
            group = GoodsChannelGroup.objects.get(id=value)
        except GoodsChannelGroup.DoesNotExist:
            raise serializers.ValidationError('频道组不存在')
        return value

    def validate_category_id(self, value):
        # 校验一级分类是否存在
        try:
            category = GoodsCategory.objects.get(id=value, parent=None)
        except GoodsCategory.DoesNotExist:
            raise serializers.ValidationError('一级分类不存在')
        return value

    # GoodsChannel.objects.create(**validated_data)


class ChannelTypeSerializer(serializers.ModelSerializer):
    """频道组的序列化器类"""
    class Meta:
        model = GoodsChannelGroup
        fields = ('id', 'name')


class ChannelCategorySerializer(serializers.ModelSerializer):
    """分类的序列化器类"""
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')

class ChannelSerializer(serializers.ModelSerializer):
    """频道的序列化器类"""
    group_id = serializers.IntegerField(label='频道组的id')
    category_id = serializers.IntegerField(label='一级分类id')

    # 关联对象的嵌套序列化
    # group_name = serializers.CharField(source="'group'.name")
    category_name = serializers.StringRelatedField(label='一级分类',source='category.name')
    """分类的序列化器类"""
    class Meta:
        model = GoodsChannel
        fields = '__all__'