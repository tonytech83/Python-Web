from django.urls import path
from rest_framework.authtoken import views as token_views

from rest_advanced.accounts.views import LoginApiView, RegisterView
from rest_advanced.api.views import api_list_authors, BookListCreateApiView

urlpatterns = (
    # path('books/', BookListCreateApiView.as_view(), name='books_list_create'),
    path('authors/', api_list_authors, name='api_list_authors'),
    path('accounts/', RegisterView.as_view(), name='api_user_create'),
    path('accounts/token/', LoginApiView.as_view(), name='api_obtain_auth_token'),
)
