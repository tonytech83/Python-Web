from django.contrib.auth import views as auth_views
from django.views import generic as views

from django.urls import reverse_lazy

from custom_auth.accounts.forms import AccountUserCreationForm


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_default_redirect_url(self):
        return reverse_lazy('index')


class RegisterUserView(views.CreateView):
    # Should overwrite the `UserCreationForm` because in `BaseUserCreationForm` default model is `User`
    # We need to create a new Form which inherits `UserCreationForm` and using our user model
    form_class = AccountUserCreationForm
    template_name = 'accounts/register.html'

    success_url = reverse_lazy('index')
