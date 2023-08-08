from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='api/', view=include('orbit.urls')),
    path(route='api-auth/', view=include('rest_framework.urls'))
]
