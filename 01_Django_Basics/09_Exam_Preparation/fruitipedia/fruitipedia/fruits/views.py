from django.urls import reverse_lazy
from django.views import generic as views

from fruitipedia.core.view_mixins import ProfileContextMixin
from fruitipedia.fruits.forms import FruitCreatFrom, FruitEditFrom, FruitDeleteFrom
from fruitipedia.fruits.models import Fruit
from fruitipedia.profiles.models import Profile


class CreateFruitView(ProfileContextMixin, views.CreateView):
    form_class = FruitCreatFrom
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()

        return super().form_valid(form)


class DetailFruitView(ProfileContextMixin, views.DetailView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/details-fruit.html'


class EditFruitView(ProfileContextMixin, views.UpdateView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/edit-fruit.html'
    form_class = FruitEditFrom

    success_url = reverse_lazy('dashboard')


class DeleteFruitView(ProfileContextMixin, views.DeleteView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/delete-fruit.html'
    form_class = FruitDeleteFrom

    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs
