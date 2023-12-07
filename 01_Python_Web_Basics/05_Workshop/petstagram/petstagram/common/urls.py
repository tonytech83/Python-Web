from django.urls import path

from petstagram.common import views

# accounts app urls.py
urlpatterns = [
    path('', views.index, name='index')
]
