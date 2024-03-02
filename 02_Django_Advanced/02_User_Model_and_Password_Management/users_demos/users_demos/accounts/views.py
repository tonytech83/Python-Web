from django.contrib.auth import views as auth_views, authenticate, login, get_user_model

from django.views import generic as views
from django.contrib.auth import forms as auth_forms

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users_demos.accounts.forms import UserCustomCreationForm

# Two important methods
# `authenticate(request, **credentials)` -> returns the user if credentials match
# 'login(request, user)` -> attaches a cookie for the authenticated user

# The correct way to get `User` class:
# If `AUTH_USER_MODEL = 'accounts.AppUser'` in `settings.py` will return `AppUser` else Django `User`
UserModel = get_user_model()


# Build-in LoginView
class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'

    # use `get_success_url(self)` to redirect to dynamic url
    # def get_success_url(self):
    #     return reverse_lazy('index')
    # The method `get_success_url(self)` should be replaced with
    # `?next={{ next }}` into template form url, example:
    # `<form action="{% url 'login-user' %}" method="POST">`


# Custom LoginView
# class LoginUserView(views.View):
#     form_class = auth_forms.AuthenticationForm
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': self.form_class(),
#         }
#
#         return render(request, 'accounts/login_user.html', context)
#
#     def post(self, request, *args, **kwargs):
#         # form = self.form_class(request.POST or None)
#         #
#         # if form.is_valid():
#         username, password = request.POST['username'], request.POST['password']
#         #
#         user = authenticate(username=username, password=password)
#         print(user)
#
#         if user is not None:
#             # Add the user to the session
#             login(request, user)
#
#         return redirect('index')


# Django do not have build-in registration view
class RegisterUserView(views.CreateView):
    form_class = UserCustomCreationForm
    # form_class = auth_forms.UserCreationForm # default form to use
    template_name = 'accounts/register_user.html'

    success_url = reverse_lazy('index')
