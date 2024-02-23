from django.views import generic as views

from fruitipedia.core.view_mixins import ProfileContextMixin
from fruitipedia.fruits.models import Fruit


class IndexView(ProfileContextMixin, views.TemplateView):
    template_name = 'main/index.html'


class DashboardView(ProfileContextMixin, views.ListView):
    queryset = Fruit.objects.all()
    template_name = 'main/dashboard.html'
