from django.views import generic as views

from world_of_speed.core.views_mixins import ProfileContextMixin


class IndexView(ProfileContextMixin, views.TemplateView):
    template_name = 'common/index.html'
