from django.urls import path, include

from petstagram.photos.views import AddPhotoView, EditPhotoView, DetailPhotoView

urlpatterns = (
    path('add/', AddPhotoView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', DetailPhotoView.as_view(), name='detail-photo'),
        path('edit/', EditPhotoView.as_view(), name='edit-photo'),
    ])),
)

# urlpatterns = (
#     path("create/", AddPhotoView.as_view(), name="create photo"),
#     path("<int:pk>/", include([
#         path("", DetailPhotoView.as_view(), name="details photo"),
#         path("edit/", EditPhotoView.as_view(), name="edit photo"),
#     ])),
# )
