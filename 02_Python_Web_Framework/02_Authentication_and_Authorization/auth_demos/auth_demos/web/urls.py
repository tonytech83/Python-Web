from django.urls import path
from django.views import generic as views

from auth_demos.web.views import index, login

urlpatterns = (
    # path('', views.TemplateView.as_view(template_name='index.html')),
    path('', index, name='index'),
    path('login/', login, name='login'),
)
