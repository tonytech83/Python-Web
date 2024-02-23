from django.urls import reverse_lazy
from django.views import generic as views

from fruitipedia.profiles.forms import ProfileCreatForm, ProfileEditForm
from fruitipedia.profiles.models import Profile


class CreateProfileView(views.CreateView):
    template_name = 'profiles/create-profile.html'
    form_class = ProfileCreatForm
    success_url = reverse_lazy('dashboard')


class DetailProfileView(views.DetailView):
    queryset = (Profile.objects.all()
                .prefetch_related('fruit_set'))

    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return Profile.objects.first()


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'profiles/edit-profile.html'
    form_class = ProfileEditForm

    success_url = reverse_lazy('details_profile')

    def get_object(self, queryset=None):
        return Profile.objects.first()


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'profiles/delete-profile.html'

    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return Profile.objects.first()
