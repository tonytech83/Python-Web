from django.shortcuts import render
from django.views import generic as auth_views

from petstagram.photos.models import Photo


class HomePageView(auth_views.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pet_photos'] = Photo.objects.all()

        return context
