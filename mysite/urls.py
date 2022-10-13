from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unity/', include('unity.urls', namespace='unity')),
    path('api/', include('unity.api.urls', namespace='api')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
