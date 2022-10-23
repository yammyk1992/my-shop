from django.urls import path, include

from .api.views.router import api_router
from .views import CartView, AddToCartView, DeleteFromCartView, EditQTYView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('edit-qty-in-cart/<str:ct_model>/<str:slug>/', EditQTYView.as_view(), name='edit_qty'),
    path('api/', include(api_router.urls)),
    ]
