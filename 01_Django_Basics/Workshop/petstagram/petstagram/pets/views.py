from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic as auth_views

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(auth_views.CreateView):
    model = Pet
    template_name = 'pets/pet-add-page.html'
    form_class = PetCreateForm

    def get_success_url(self):
        return reverse('details-pet', kwargs={'username': 'admin', 'pet_slug': self.object.slug})


class EditPetView(auth_views.UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    form_class = PetEditForm

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        # username = self.kwargs.get('username')
        pet_slug = self.kwargs.get('pet_slug')

        # user = get_object_or_404(User, username=username)
        pet = get_object_or_404(Pet, slug=pet_slug)

        return pet

    def get_success_url(self):
        return reverse('details-pet', kwargs={'username': 'admin', 'pet_slug': self.object.slug})


class DetailsPetView(auth_views.DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        # username = self.kwargs.get('username')
        pet_slug = self.kwargs.get('pet_slug')

        # user = get_object_or_404(User, username=username)
        pet = get_object_or_404(Pet, slug=pet_slug)

        return pet


class DeletePetView(auth_views.DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = PetDeleteForm
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pet_slug = self.kwargs.get('pet_slug')

        return get_object_or_404(Pet, slug=pet_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = PetDeleteForm(instance=self.object)

        return context
