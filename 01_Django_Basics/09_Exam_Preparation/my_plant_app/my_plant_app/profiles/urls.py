from django.urls import path

from my_plant_app.profiles.views import CreateProfileView, DetailProfileView, EditProfileView, DeleteProfileView

urlpatterns = (
    path('create/', CreateProfileView.as_view(), name='create-profile'),
    path('details/', DetailProfileView.as_view(), name='details-profile'),
    path('edit/', EditProfileView.as_view(), name='edit-profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete-profile'),
)
