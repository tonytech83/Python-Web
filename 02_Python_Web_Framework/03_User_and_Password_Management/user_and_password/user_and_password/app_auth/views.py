# app_auth/views.py
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from django.utils.translation import gettext_lazy as _

"""
from django.contrib.auth import views as auth_views -> LoginView, LogoutView and etc.
from django.contrib.auth import forms as auth_forms -> UserCreationForm and etc.
"""


class RegisterUserForm(auth_forms.UserCreationForm):
    # to take more fields form `User` model we should overwrite `Meta`
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    # Additional new fields
    consent = forms.BooleanField()

    # customize existing fields
    # change `label` and `help_text` from `auth_forms.UserCreationForm` -> `BaseUserCreationForm`
    # should be loaded `from django.utils.translation import gettext_lazy as _`
    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please."),
    )

    # customize existing fields - change `help_text` of `username` and `password1`
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _("It works!")
        self.fields['username'].help_text = _("Please enter your name")


class RegisterUserView(views.CreateView):
    # Minimum
    template_name = 'app_auth/register.html'
    # Static way of providing Form
    form_class = RegisterUserForm
    # Static way of providing `success_url`
    success_url = reverse_lazy('register-user')

    # Additional customization
    # - login automatically after registration
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    # Dynamic way of providing `success_url`
    # def get_success_url(self):
    #     pass

    # Dynamic way of providing Form
    # def get_form_kwargs(self):
    #     if condition1:
    #         return Condition1Form
    #     elif condition2:
    #         return Condition2Form
    #     else:
    #         return Condition3Form


class LoginUserView(auth_views.LoginView):
    # Minimum
    template_name = 'app_auth/login.html'

    # Additional customization


UserModel = get_user_model()


#
class ViewWithPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'app_auth/users_list.html'


# Using `auth_mixins.LoginRequiredMixin` to restrict non login user to access the view
class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'

    # The proper way is to setup `LOGIN_URL` in `settings.py`
    # `login_url` is URL only for this view:
    # login_url = reverse_lazy('aaa/aaa/a.html')


class LogoutUserView(auth_views.LogoutView):
    pass
