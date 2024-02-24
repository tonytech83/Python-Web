from django.urls import path, include

from world_of_speed.cars.views import CatalogueView, CreateCarView, DetailsCarView, EditCarView, DeleteCarView

urlpatterns = (
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('create/', CreateCarView.as_view(), name='create-car'),
    path('<int:pk>/', include([
        path('details/', DetailsCarView.as_view(), name='details-car'),
        path('edit', EditCarView.as_view(), name='edit-car'),
        path('delete/', DeleteCarView.as_view(), name='delete-car'),
    ])),
)
