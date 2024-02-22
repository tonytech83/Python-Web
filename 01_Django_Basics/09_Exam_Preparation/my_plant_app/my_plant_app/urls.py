from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_plant_app.common.urls')),
    path('profile/', include('my_plant_app.profiles.urls')),
    path('', include('my_plant_app.plants.urls')),
]
