from django.urls import path, include

from .api.views.router import api_router
from .views import CategoryDetailView

urlpatterns = [
    path('category/<str:slug>/',
         CategoryDetailView.as_view(),
         name='category_detail'),
    path('api/', include(api_router.urls)),
]
