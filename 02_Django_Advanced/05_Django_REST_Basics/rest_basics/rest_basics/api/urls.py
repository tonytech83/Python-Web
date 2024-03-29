from django.urls import path

from rest_basics.api.views import api_list_books, BookListApiView, BookUpdateApiView

urlpatterns = (
    path('books/', BookListApiView.as_view(), name='api_list_create_books'),
    path('books/<int:pk>/', BookUpdateApiView.as_view(), name='api_update_book'),
)
