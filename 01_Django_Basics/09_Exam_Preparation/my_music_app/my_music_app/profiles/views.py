from django.urls import reverse_lazy
from django.views import generic as views

from my_music_app.profiles.models import Profile


class ProfileDetailView(views.DetailView):
    queryset = (Profile.objects.all()
                .prefetch_related('album_set'))

    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return Profile.objects.first()


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'

    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return Profile.objects.first()
