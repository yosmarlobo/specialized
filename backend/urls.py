from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls.conf import include

from .frontend import urls as frontend_urls

urlpatterns = [
    path("", include(frontend_urls)),

    path('admin/', admin.site.urls),
]
# configuracion de rutas de imagenes
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
