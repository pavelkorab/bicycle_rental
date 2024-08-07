from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/bikes/', include('bikes.urls')),
    path('api/v1/rentals/', include('rentals.urls')),
]