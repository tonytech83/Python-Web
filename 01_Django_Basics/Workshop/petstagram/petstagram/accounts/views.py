from django import forms
from django.contrib.auth import get_user_model, login, logout

from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreationForm
from petstagram.accounts.models import Profile

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    redirect_authenticated_user = True


class RegisterUserView(views.CreateView):
    form_class = PetstagramUserCreationForm
    template_name = 'accounts/register-page.html'

    success_url = reverse_lazy('home-page')

    # register to log in automation
    def form_valid(self, form):
        # `form_valid` will call `save`
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


def logout_user(request):
    logout(request)

    return redirect('home-page')


class ProfileDetailsView(views.DetailView):
    queryset = (Profile.objects
                .all()
                .prefetch_related('user'))

    template_name = 'accounts/profile-details-page.html'


class EditProfileView(views.UpdateView):
    queryset = (Profile.objects
                .all()
                .prefetch_related('user'))

    template_name = 'accounts/profile-edit-page.html'
    fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture')

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk},
        )

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #
    #     form.fields['date_of_birth'].widget = forms.DateInput()
    #
    #     return form


class DeleteProfileView(auth_views.FormView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile-delete-page.html'
