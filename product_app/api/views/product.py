from rest_framework.viewsets import ModelViewSet

from product_app.api.serializers.product import SportSerializer, TVSerializer, GoodsSerializer, ToysSerializer
from product_app.models import Sport, TV, Goods, Toys


class SportViewSet(ModelViewSet):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()


class TVViewSet(ModelViewSet):
    serializer_class = TVSerializer
    queryset = TV.objects.all()


class GoodsViewSet(ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()


class ToysViewSet(ModelViewSet):
    serializer_class = ToysSerializer
    queryset = Toys.objects.all()
