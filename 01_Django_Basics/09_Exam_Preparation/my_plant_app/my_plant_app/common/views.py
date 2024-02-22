from django.views import generic as views

from my_plant_app.core.views_mixins import ProfileContextMixin
from my_plant_app.plants.models import Plant


class HomePageView(ProfileContextMixin, views.TemplateView):
    template_name = 'common/home-page.html'


class CatalogView(ProfileContextMixin, views.ListView):
    queryset = Plant.objects.all()
    template_name = 'common/catalogue.html'
