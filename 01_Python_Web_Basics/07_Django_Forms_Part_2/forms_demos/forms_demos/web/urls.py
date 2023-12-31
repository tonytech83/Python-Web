from django.urls import path

from forms_demos.web import views

urlpatterns = (
    path('', views.index, name='index'),
)
