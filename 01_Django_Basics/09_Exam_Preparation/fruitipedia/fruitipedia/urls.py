

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruitipedia.main.urls')),
    path('fruit/', include('fruitipedia.fruits.urls')),
    path('profile/', include('fruitipedia.profiles.urls')),
]
