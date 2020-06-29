from django.conf.urls import url

from meiduo_admin.views import users, statistical, channels, skus, spus, orders, permissions

urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthView.as_view()),

    # 数据统计
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$', statistical.UserDayIncrementView.as_view()),
    url(r'^statistical/day_active/$', statistical.UserDayActiveView.as_view()),
    url(r'^statistical/day_orders/$', statistical.UserDayOrdersView.as_view()),
    url(r'^statistical/month_increment/$', statistical.UserMonthIncrementView.as_view()),
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayViewsView.as_view()),

    # 用户管理
    url(r'^users/$', users.UserInfoView.as_view()),

    # 频道管理
    url(r'^goods/channel_types/$', channels.ChannelTypesView.as_view()),
    url(r'^goods/categories/(?P<pk>\d+)/$', channels.Channel.as_view()),
    url(r'^goods/categories/$', channels.ChannelCategoriesView.as_view()),
    url(r'^goods/channels/$', channels.ChannelsView.as_view()),

    # 图片管理
    url(r'^skus/simple/$', skus.SKUSimpleView.as_view()),

    # SKU管理
    url(r'^goods/simple/$', spus.SPUGoodsView.as_view()),
    url(r'^goods/specs/simple/$', spus.SPUGoodsSpecView.as_view({
        'get':'list'
    })),
    url(r'^goods/(?P<pk>\d+)/specs/$', spus.SPUSpecView.as_view()),
    url(r'^goods/specs/$', spus.SPUGoodsSpecView.as_view({
        'get': 'list', 'post':'create'
    })),
    url(r'^goods/specs/(?P<pk>\d+)/$', spus.SPUGoodsSpecView.as_view({
        'get': 'retrieve','put': 'update','delete': 'destroy'
    })),

    # SPU管理
    url(r'^goods/$', spus.SPUView.as_view()),
    url(r'^goods/(?P<pk>\d+)/$', spus.SPUSimpleView.as_view({
        'get': 'list','put': 'update'})),
    # 规格选项管理
    url(r'^specs/options/(?P<pk>\d+)/$', spus.SPCEOptionView.as_view({
        'get': 'retrieve','put': 'update'
    })),

    # 品牌管理
    url(r'^goods/brands/$', spus.GoodsBrandsView.as_view({
        'get': 'list','post':'create'
    })),
    url(r'^goods/brands/(?P<pk>\d+)/$', spus.GoodsBrandsView.as_view({
        'get': 'retrieve','put': 'update','delete':'destroy'
    })),

    # 权限管理
    url(r'^permission/content_types/$', permissions.PermissionViewSet.as_view({
        'get': 'content_types'
    })),

    # 用户组管理
    url(r'^permission/simple/$', permissions.GroupViewSet.as_view({
        'get': 'simple'
    })),

    # 管理员管理
    url(r'^permission/groups/simple/$', permissions.AdminViewSet.as_view({
        'get': 'simple'
    })),

    # 订单管理
    # url(r'^orders/(?P<keyword>\d+)/$', orders.OrdersView.as_view({
    #     'get': 'list'
    # })),
]

# 频道管理
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('goods/channels', channels.ChannelViewSet, base_name='channels')
urlpatterns += router.urls

# 图片管理
router = DefaultRouter()
router.register('skus/images', skus.SKUImageViewSet, base_name='images')
urlpatterns += router.urls

# SKU管理
router = DefaultRouter()
router.register('skus', skus.SKUViewSet, base_name='skus')
urlpatterns += router.urls

# 订单管理
router = DefaultRouter()
router.register('orders', orders.OrdersViewSet, base_name='orders')
urlpatterns += router.urls

# 权限管理
router = DefaultRouter()
router.register('permission/perms', permissions.PermissionViewSet, base_name='perms')
urlpatterns += router.urls

# 用户组管理
router = DefaultRouter()
router.register('permission/groups', permissions.GroupViewSet, base_name='groups')
urlpatterns += router.urls

# 管理员管理
router = DefaultRouter()
router.register('permission/admins', permissions.AdminViewSet, base_name='admins')
urlpatterns += router.urls

# spu管理
router = DefaultRouter()
router.register('goods', spus.SPUSimpleView, base_name='spus')
urlpatterns += router.urls

# 规格选项管理
router = DefaultRouter()
router.register('specs/options', spus.SPCEOptionView, base_name='options')
urlpatterns += router.urls

# 规格管理
router = DefaultRouter()
router.register('goods/specs', spus.SPUGoodsSpecView, base_name='specs')
urlpatterns += router.urls

# 品牌管理
router = DefaultRouter()
router.register('goods/brands', spus.SPUGoodsSpecView, base_name='brands')
urlpatterns += router.urls