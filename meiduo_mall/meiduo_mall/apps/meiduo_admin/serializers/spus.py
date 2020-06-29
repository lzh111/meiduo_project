from rest_framework import serializers

from goods.models import SPU, SPUSpecification, SpecificationOption, Brand


class SPUSimpleSerializer(serializers.ModelSerializer):
    """spu序列化器类"""
    class Meta:
        model = SPU
        fields = ('id', 'name')


class SpecOptionSerializer(serializers.ModelSerializer):
    """规格选项序列化器类"""
    class Meta:
        model = SpecificationOption
        fields = ('id', 'value')


class SPUSpecSerializer(serializers.ModelSerializer):
    """SPU规格序列化器类"""
    spu = serializers.StringRelatedField(source='spu_id.name',read_only=True)
    class Meta:
        model = SPUSpecification
        fields = '__all__'


class SPUSpecificationSerializer(serializers.ModelSerializer):
    # 关联嵌套返回spu表的商品名
    spu = serializers.StringRelatedField(read_only=True)
    # 返回关联spu的id值
    spu_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SPUSpecification  # 商品规格表关联了spu表的外键spu
        fields = '__all__'

class SPUSerializer(serializers.ModelSerializer):
    # 品牌格式化

    # 关联对象的嵌套序列化
    # group_name = serializers.CharField(source="'group'.name")
    category1_name = serializers.StringRelatedField(source='category1_id.name')
    category2_name = serializers.StringRelatedField(source='category2_id.name')
    category3_name = serializers.StringRelatedField(source='category3_id.name')
    # category1_id = serializers.IntegerField()
    brand_name = serializers.StringRelatedField(source='brand_id.name')
    class Meta:
        model = SPU  # 商品规格表关联了spu表的外键spu
        fields = '__all__'



class SPCEOptionSerializer(serializers.ModelSerializer):
    '''格选选项序列化器'''
    spec_name = serializers.CharField(source='spec_id.name',read_only=True)

    class Meta:
        model = SpecificationOption  # 商品规格表关联了spu表的外键spu
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    '''品牌管理序列化器'''

    class Meta:
        model = Brand  # 商品规格表关联了spu表的外键spu
        fields = '__all__'
