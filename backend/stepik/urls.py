from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('api/v1/', include(('apps.core.api.urls', 'apps.core'), namespace='core-api')),
    path('admin/', admin.site.urls),
]
