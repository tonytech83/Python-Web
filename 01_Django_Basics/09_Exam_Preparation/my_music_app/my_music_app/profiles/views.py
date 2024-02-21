from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from my_music_app.profiles.models import Profile


class ProfileDetailView(views.DetailView):
    queryset = (Profile.objects.all()
                .prefetch_related('album_set'))

    template_name = 'profile/profile-details.html'

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.first()

        if profile:
            context = {
                'profile': profile,
            }

            return render(request, self.template_name, context)


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'

    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
