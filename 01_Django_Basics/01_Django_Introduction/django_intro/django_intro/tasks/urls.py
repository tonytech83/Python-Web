from django.urls import path

from django_intro.tasks.views import index

urlpatterns = (
    path('', index, name='index'),
)
