from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from forms_advanced import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('forms_advanced.web.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
