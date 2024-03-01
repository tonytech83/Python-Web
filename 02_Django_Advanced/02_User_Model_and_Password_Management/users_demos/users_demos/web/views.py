from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse

from django.views import generic as views


def index(request):
    return HttpResponse("It works!")


@login_required
def about(request):
    return HttpResponse(f"It's about that, {request.user}!")


class TeamView(auth_mixins.LoginRequiredMixin, views.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f"{request.user}'s team!")
