from django.urls import path

from forms_basic.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
