from django.contrib.auth import get_user_model, login

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreationForm

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    redirect_authenticated_user = True


class RegisterUserView(views.CreateView):
    form_class = PetstagramUserCreationForm
    template_name = 'accounts/register-page.html'

    success_url = reverse_lazy('home-page')

    # register to log in automation
    # Should make changes in `PetstagramUserCreationForm`
    def form_valid(self, form):
        # `form_valid` will call `save`
        result = super().form_valid(form)

        login(self.request, form.user)

        return result


class ShowProfileDetailsView(auth_views.FormView):
    pass
    # model = UserModel
    # template_name = 'accounts/profile-details-page.html'


class EditProfileView(auth_views.FormView):
    pass
    # template_name = 'accounts/profile-edit-page.html'


class DeleteProfileView(auth_views.FormView):
    pass
    # template_name = 'accounts/profile-delete-page.html'
