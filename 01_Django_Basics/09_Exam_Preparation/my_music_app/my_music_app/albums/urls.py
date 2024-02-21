from django.urls import path, include

from my_music_app.albums.views import AlbumCreateView, AlbumDetailsView, AlbumEditView, AlbumDeleteView

urlpatterns = (
    path('add/', AlbumCreateView.as_view(), name='add-album'),
    path('<int:pk>/', include([
        path('details/', AlbumDetailsView.as_view(), name='details-album'),
        path('edit/', AlbumEditView.as_view(), name='edit-album'),
        path('delete/', AlbumDeleteView.as_view(), name='delete-album'),
    ])),
)
