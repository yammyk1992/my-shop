from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .api.views.router import api_router
from .views import add_review

urlpatterns = [
                  path('api/', include(api_router.urls)),
                  path('review/<str:ct_model>/<str:slug>/',
                       add_review,
                       name='add_review'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
