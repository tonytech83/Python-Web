from django.urls import path

from rest_advanced.api.views import BookListCreateApiView

urlpatterns = (
    path('books/', BookListCreateApiView.as_view(), name='api_list_create_books'),
)
