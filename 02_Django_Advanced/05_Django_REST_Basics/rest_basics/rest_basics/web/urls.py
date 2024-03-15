from django.http import HttpResponse
from django.urls import path

from rest_basics.web.views import IndexView

urlpatterns = (
    # path('', lambda request: HttpResponse('It works!'), name='index'),  # valid view :)
    path('', IndexView.as_view(), name='index'),
)
