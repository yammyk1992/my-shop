from rest_framework import routers

from product_app.api.views.product import GoodsViewSet, TVViewSet, SportViewSet, ToysViewSet


api_router = routers.DefaultRouter()
api_router.register('goods_product', GoodsViewSet)
api_router.register('toys_product', ToysViewSet)
api_router.register('sport_product', SportViewSet)
api_router.register('tv_product', TVViewSet)

