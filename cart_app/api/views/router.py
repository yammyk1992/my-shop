from rest_framework import routers

from cart_app.api.views.cart import CartProductViewSet, CartViewSet

api_router = routers.DefaultRouter()
api_router.register('cart', CartViewSet)
api_router.register('cart_with_products', CartProductViewSet)
