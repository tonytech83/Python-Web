from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_music_app.common.urls')),
    path('album/', include('my_music_app.albums.urls')),
    path('profile/', include('my_music_app.profiles.urls')),
]
