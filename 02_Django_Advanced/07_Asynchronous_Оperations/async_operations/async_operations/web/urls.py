from django.urls import path

from async_operations.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
