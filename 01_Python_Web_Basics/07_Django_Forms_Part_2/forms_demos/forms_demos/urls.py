from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forms_demos.web.urls')),
]

# working with media files
# the image is accessible on URL: http://127.0.0.1:8000/media/persons/awo66eW_700b.jpg
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
