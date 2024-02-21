from django.urls import path

from my_music_app.profiles.views import ProfileDetailView, ProfileDeleteView

urlpatterns = (
    path('details/', ProfileDetailView.as_view(), name='details-profile'),
    path('delete/', ProfileDeleteView.as_view(), name='delete-profile'),
)
