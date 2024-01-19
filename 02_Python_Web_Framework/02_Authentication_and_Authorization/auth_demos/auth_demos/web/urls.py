from django.urls import path
from django.views import generic as views

from auth_demos.web.views import index, login_user, logout_user

urlpatterns = (
    # path('', views.TemplateView.as_view(template_name='index.html')),
    path('', index, name='index'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
)
