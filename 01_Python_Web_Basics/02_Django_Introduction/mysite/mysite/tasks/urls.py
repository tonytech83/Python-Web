from django.urls import path
from mysite.tasks import views

urlpatterns = [
    path('', views.index)
]
