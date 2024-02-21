from django.urls import path

from my_music_app.common.views import HomePageView

urlpatterns = (
    path('', HomePageView.as_view(), name='home-page'),
)
