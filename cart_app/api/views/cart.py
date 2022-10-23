from rest_framework import filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from cart_app.api.serializers.cart import CartSerializer, CartProductSerializer
from cart_app.models import Cart, CartProduct


class CartViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    filter_backends = [filters.OrderingFilter]


class CartProductViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = CartProductSerializer
    queryset = CartProduct.objects.all()
    filter_backends = [filters.OrderingFilter]
