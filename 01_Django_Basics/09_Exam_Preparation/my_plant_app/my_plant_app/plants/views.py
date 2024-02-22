from django.urls import reverse_lazy
from django.views import generic as views

from my_plant_app.core.views_mixins import ProfileContextMixin
from my_plant_app.plants.forms import PlantCreationForm, PlantEditForm, PlantDeleteForm
from my_plant_app.plants.models import Plant


class CreatePlantView(ProfileContextMixin, views.CreateView):
    form_class = PlantCreationForm
    template_name = 'plants/create-plant.html'
    success_url = reverse_lazy('catalogue')


class DetailPlantView(ProfileContextMixin, views.DetailView):
    queryset = Plant.objects.all()
    template_name = 'plants/plant-details.html'


class EditPlantView(ProfileContextMixin, views.UpdateView):
    queryset = Plant.objects.all()
    template_name = 'plants/edit-plant.html'
    form_class = PlantEditForm

    success_url = reverse_lazy('catalogue')


class DeletePlantView(ProfileContextMixin, views.DeleteView):
    queryset = Plant.objects.all()
    template_name = 'plants/delete-plant.html'
    form_class = PlantDeleteForm

    success_url = reverse_lazy('catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs
