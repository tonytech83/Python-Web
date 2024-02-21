from django.shortcuts import render, redirect
from django.views import generic as views

from my_music_app.albums.models import Album
from my_music_app.profiles.forms import ProfileCreateForm
from my_music_app.profiles.models import Profile


class HomePageView(views.TemplateView):
    template_name = 'common/home-no-profile.html'

    def get(self, request, *args, **kwargs):
        albums = Album.objects.all()
        form = ProfileCreateForm()
        profile = Profile.objects.first()

        if profile:
            self.template_name = 'common/home-with-profile.html'

            context = {
                'object_list': albums,
                'profile': profile,
            }

            return render(self.request, self.template_name, context)

        context = {
            'form': form,
            'object_list': albums,
        }

        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home-page')

        context = {
            'form': form,
        }

        return render(self.request, self.template_name, context)
