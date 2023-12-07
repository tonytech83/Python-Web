from django.urls import path, include

from petstagram.photos import views

# photos app urls.py
urlpatterns = [
    path('add/', views.add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('', views.details_photo, name='details photo'),
        path('edit/', views.edit_photo, name='edit photo')
    ]))
]
