from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_basics.web.urls')),
    path('api/', include('rest_basics.api.urls')),
]
