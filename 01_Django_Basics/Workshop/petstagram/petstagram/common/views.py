from django.shortcuts import render
from django.views import generic as auth_views


class HomePageView(auth_views.TemplateView):
    template_name = 'common/home-page.html'
