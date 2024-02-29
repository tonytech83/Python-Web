from django.urls import path

from users_demos.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
