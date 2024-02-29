from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy


# Two important methods
# `authenticate(request, **credentials)` -> returns the user if credentials match
# 'login(request, user)` -> attaches a cookie for the authenticated user
class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'

    def get_success_url(self):
        return reverse_lazy('index')
