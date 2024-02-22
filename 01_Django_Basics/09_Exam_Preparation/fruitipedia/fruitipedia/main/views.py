from django.views import generic as views

from fruitipedia.core.view_mixins import ProfileContextMixin


class IndexView(ProfileContextMixin, views.TemplateView):
    template_name = 'main/index.html'


class DashboardView(views.TemplateView):
    pass
