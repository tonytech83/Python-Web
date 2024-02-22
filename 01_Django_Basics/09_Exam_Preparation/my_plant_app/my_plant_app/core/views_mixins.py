from django.views.generic.base import ContextMixin

from my_plant_app.profiles.models import Profile


class ProfileContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
