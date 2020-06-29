from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from django.utils import timezone

from goods.models import GoodsVisitCount
from meiduo_admin.serializers.statistical import GoodsVisitSerializer
from users.models import User


# GET /meiduo_admin/statistical/total_count/
class UserTotalCountView(APIView):
    # 只有管理员才能进行访问
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        统计网站的总用户数:
        1. 查询数据库统计网站的总用户数
        2. 返回响应的数据
        """
        # 1. 查询数据库统计网站的总用户数
        count = User.objects.count()

        # 2. 返回响应的数据
        # 年-月-日 时:分:秒
        now_date = timezone.now()

        response_data = {
            'count': count,
            # 年-月-日
            'date': now_date.date()
        }

        return Response(response_data)


# GET /meiduo_admin/statistical/day_increment/
class UserDayIncrementView(APIView):
    # 只有管理员才能进行访问
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        统计网站的日增用户数:
        1. 查询数据库统计网站的日增用户数
        2. 返回响应数据
        """
        # 1. 查询数据库统计网站的日增用户数
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(date_joined__gte=now_date).count()

        # 2. 返回响应数据
        response_data = {
            'count': count,
            'date': now_date.date()
        }

        return Response(response_data)


# GET /meiduo_admin/statistical/day_active/
class UserDayActiveView(APIView):
    # 只有管理员才能进行访问
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        统计网站日活用户数:
        1. 查询数据库统计网站日活用户数
        2. 返回响应数据
        """
        # 1. 查询数据库统计网站日活用户数
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(last_login__gte=now_date).count()

        # 2. 返回响应数据
        response_data = {
            'count': count,
            'date': now_date.date()
        }

        return Response(response_data)


# GET /meiduo_admin/statistical/day_orders/
class UserDayOrdersView(APIView):
    # 只有管理员才能进行访问
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        统计网站的日下单用户数:
        1. 查询数据库统计日下单用户的数量
        2. 返回响应的数据
        """
        # 1. 查询数据库统计日下单用户的数量
        # 下单用户条件：和用户关联的订单的创建时间大于等于统计当天的00:00:00
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # user
        # user.orders.all()[0].create_time
        count = User.objects.filter(orders__create_time__gte=now_date).distinct().count()

        # 2. 返回响应的数据
        response_data = {
            'count': count,
            'date': now_date.date()
        }

        return Response(response_data)


# GET /meiduo_admin/statistical/month_increment/
class UserMonthIncrementView(APIView):
    # 只有管理员才能进行访问
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        统计网站近30天每日新增用户的数量:
        1. 查询数据库统计网站最近30天每日新增的用户数量
        2. 返回响应的数据
        """
        # 1. 查询数据库统计网站最近30天每日新增的用户数量
        # 结束时间
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # 起始时间: now_date - 29天
        begin_date = now_date - timezone.timedelta(days=29)

        # 当天日期
        current_date = begin_date

        # 新增用户的数量
        month_li = []

        while current_date <= now_date:
            # 次日时间
            next_date = current_date + timezone.timedelta(days=1)
            # 统计当天的新增用户数量
            count = User.objects.filter(date_joined__gte=current_date,
                                        date_joined__lt=next_date).count()

            month_li.append({
                'count': count,
                'date': current_date.date()
            })

            current_date += timezone.timedelta(days=1)

        # 2. 返回响应的数据
        return Response(month_li)


# GET /meiduo_admin/statistical/goods_day_views/
class GoodsDayViewsView(ListAPIView):
    # 只有管理员才能进行访问
    permission_classes = [IsAdminUser]

    serializer_class = GoodsVisitSerializer
    # queryset = GoodsVisitCount.objects.filter(date=now_date)

    def get_queryset(self):
        """返回日分类商品访问数据的查询集"""
        now_date = timezone.now().date()
        print(now_date)
        queryset = GoodsVisitCount.objects.filter(date='2020-05-01')
        return queryset

    # def get(self, request):
    #     return self.list(request)

    # def get(self, request):
    #     """
    #     获取日分类商品访问量数据:
    #     1. 查询获取当天日分类商品访问量的数据
    #     2. 将数据序列化并返回
    #     """
    #     # 1. 查询获取当天日分类商品访问量的数据
    #     goods_visits = self.get_queryset()
    #
    #     # 2. 将数据序列化并返回
    #     serializer = self.get_serializer(goods_visits, many=True)
    #     return Response(serializer.data)
















