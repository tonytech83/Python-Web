from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cbv_basic.web.urls')),
    path('custom/', include('cbv_basic.custom_class_base_view.urls')),
]
