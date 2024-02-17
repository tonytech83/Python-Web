from django.urls import path

from petstagram.common.views import HomePageView, like_pet_photo

urlpatterns = (
    path('', HomePageView.as_view(), name='home-page'),
    path('pet_photo_like/<int:pk>', like_pet_photo, name='like-pet-photo')
)
