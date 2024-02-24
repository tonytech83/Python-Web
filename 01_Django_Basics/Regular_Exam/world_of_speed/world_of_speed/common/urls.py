from django.urls import path

from world_of_speed.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
