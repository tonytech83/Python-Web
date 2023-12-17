from django.urls import path, include

from petstagram.pets import views

# pets app urls.py
urlpatterns = [
    path('add/', views.add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.details_details, name='details pet'),
        path('edit/', views.edit_pet, name='edit pet'),
        path('delete/', views.delete_pet, name='delete pet')
    ]))
]
