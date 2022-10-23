from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from django.conf.urls.static import static

from .api.views.router import api_router
from .views import ProductDetailView

urlpatterns = [
                  path('api/', include(api_router.urls)),
                  path('products/<str:ct_model>/<str:slug>',
                       ProductDetailView.as_view(),
                       name='product_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
