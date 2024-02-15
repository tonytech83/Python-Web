from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.urls')),
    path('accounts/', include('petstagram.accounts.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('photos/', include('petstagram.photos.urls')),
]

# With this code we will have access to media files
# For example, we can access `the_cat.jpg` on url: http://127.0.0.1:8000/media/photos/the_cat.jpg
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
