from django.urls import path

from rest_advanced.api.views import api_list_authors

urlpatterns = (
    path('authors/', api_list_authors, name='api_list_authors'),
)
