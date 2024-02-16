from django.urls import path, include

from petstagram.photos.views import AddPhotoView, detail_photo, EditPhotoView

urlpatterns = (
    path('add/', AddPhotoView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', detail_photo, name='detail-photo'),
        path('<int:pk>/edit/', EditPhotoView.as_view(), name='edit-photo'),
    ])),
)
