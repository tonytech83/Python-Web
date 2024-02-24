from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed.cars.forms import CarCreationForm, CarEditForm, CarDeleteForm
from world_of_speed.cars.models import Car
from world_of_speed.core.views_mixins import ProfileContextMixin
from world_of_speed.profiles.models import Profile


class CatalogueView(ProfileContextMixin, views.ListView):
    queryset = Car.objects.all()
    template_name = 'cars/catalogue.html'


class CreateCarView(ProfileContextMixin, views.CreateView):
    form_class = CarCreationForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()

        return super().form_valid(form)


class DetailsCarView(ProfileContextMixin, views.DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'


class EditCarView(ProfileContextMixin, views.UpdateView):
    queryset = Car.objects.all()
    form_class = CarEditForm
    template_name = 'cars/car-edit.html'

    success_url = reverse_lazy('catalogue')


class DeleteCarView(ProfileContextMixin, views.DeleteView):
    queryset = Car.objects.all()
    template_name = 'cars/car-delete.html'
    form_class = CarDeleteForm

    success_url = reverse_lazy('catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs
