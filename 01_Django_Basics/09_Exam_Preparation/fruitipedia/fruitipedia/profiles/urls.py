from django.urls import path

from fruitipedia.profiles.views import CreateProfileView, DetailProfileView, EditProfileView, DeleteProfileView

urlpatterns = (
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('details/', DetailProfileView.as_view(), name='details_profile'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete_profile'),
)
