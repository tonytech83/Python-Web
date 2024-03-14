from django.http import HttpResponse
from django.urls import path

urlpatterns = (
    path('', lambda request: HttpResponse('It works!'), name='index'),  # valid view :)
)
