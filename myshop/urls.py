from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from .views import HomeView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', HomeView.as_view(), name='home'),
                  path('', include('product_app.urls')),
                  path('', include('cart_app.urls')),
                  path('', include('category_app.urls')),
                  path('', include('profile_app.urls')),
                  path('', include('review_app.urls')),
                  path('', include('order_app.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
