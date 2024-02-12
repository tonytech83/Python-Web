from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_and_password.web.urls')),
    path('auth/', include('user_and_password.app_auth.urls')),
]
