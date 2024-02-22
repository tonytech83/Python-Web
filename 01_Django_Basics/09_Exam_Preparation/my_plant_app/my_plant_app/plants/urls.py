from django.urls import path

from my_plant_app.plants.views import CreatePlantView, DetailPlantView, EditPlantView, DeletePlantView

urlpatterns = (
    path('create/', CreatePlantView.as_view(), name='create-plant'),
    path('details/<int:pk>/', DetailPlantView.as_view(), name='detail-plant'),
    path('edit/<int:pk>/', EditPlantView.as_view(), name='edit-plant'),
    path('delete/<int:pk>/', DeletePlantView.as_view(), name='delete-plant'),
)
