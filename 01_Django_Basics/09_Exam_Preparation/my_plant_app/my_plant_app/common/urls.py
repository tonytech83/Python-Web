from django.urls import path

from my_plant_app.common.views import HomePageView, CatalogView

urlpatterns = (
    path('', HomePageView.as_view(), name='home-page'),
    path('catalogue/', CatalogView.as_view(), name='catalogue'),
)
