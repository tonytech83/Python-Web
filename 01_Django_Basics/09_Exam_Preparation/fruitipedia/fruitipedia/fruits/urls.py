from django.urls import path, include

from fruitipedia.fruits.views import CreateFruitView, DetailFruitView, EditFruitView, DeleteFruitView

urlpatterns = (
    path('create/', CreateFruitView.as_view(), name='create-fruit'),
    path('<int:pk>/', include([
        path('details/', DetailFruitView.as_view(), name='detail-fruit'),
        path('edit/', EditFruitView.as_view(), name='edit-fruit'),
        path('delete/', DeleteFruitView.as_view(), name='delete-fruit'),
    ])),
)
