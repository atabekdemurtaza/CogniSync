from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='api/', view=include('orbit.urls', namespace='orbit')),
    path(route='api-auth/', view=include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
