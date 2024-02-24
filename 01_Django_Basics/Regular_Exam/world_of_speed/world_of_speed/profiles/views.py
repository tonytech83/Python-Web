from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed.profiles.forms import ProfileCreationForm, ProfileEditForm
from world_of_speed.profiles.models import Profile


class CreateProfileView(views.CreateView):
    form_class = ProfileCreationForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('catalogue')


class DetailsProfileView(views.DetailView):
    queryset = (Profile.objects.all()
                .prefetch_related('car_set'))

    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        total_cost = sum(car.price for car in profile.car_set.all())

        context['total_cost'] = total_cost
        return context


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-edit.html'
    form_class = ProfileEditForm

    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return Profile.objects.first()


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-delete.html'

    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return Profile.objects.first()
