from django.urls import reverse_lazy
from django.views import generic as views

from my_plant_app.core.views_mixins import ProfileContextMixin
from my_plant_app.plants.models import Plant
from my_plant_app.profiles.forms import ProfileCreateForm, ProfileEditForm
from my_plant_app.profiles.models import Profile


class CreateProfileView(views.CreateView):
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue')


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_stars'] = Plant.objects.all().count()

        return context

    def get_object(self, queryset=None):
        return Profile.objects.first()


class EditProfileView(ProfileContextMixin, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'profiles/edit-profile.html'
    form_class = ProfileEditForm

    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return Profile.objects.first()


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'profiles/delete-profile.html'

    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        Plant.objects.all().delete()

        return response
