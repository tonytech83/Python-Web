from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django.urls import reverse_lazy
from django.views import generic as auth_views


class RegisterView(auth_views.CreateView):
    model = User
    template_name = 'accounts/register-page.html'
    fields = '__all__'


class LoginView(auth_views.FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('common/home_page.html')

    def form_valid(self, form):
        # Authenticate user
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super().form_valid(form)
            else:
                form.add_error(None, "This account is inactive.")
        else:
            form.add_error(None, "Invalid username or password.")

        return super().form_invalid(form)


class ShowProfileDetailsView(auth_views.DetailView):
    model = User
    template_name = 'accounts/profile-details-page.html'


class EditProfileView(auth_views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'


class DeleteProfileView(auth_views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
