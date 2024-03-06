from django.contrib.auth import views as auth_views
from django.shortcuts import render


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class RegisterUserView():
    pass
