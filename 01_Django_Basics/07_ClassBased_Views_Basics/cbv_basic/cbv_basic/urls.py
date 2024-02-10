from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cbv_basic import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cbv_basic.web.urls')),
    path('custom/', include('cbv_basic.custom_class_base_view.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
