from django.urls import path

from .views import OrderView, MakeOrderView

urlpatterns = [
    path('checkout/', OrderView.as_view(), name='checkout'),
    path('make_order/', MakeOrderView.as_view(), name='make_order'),
]
