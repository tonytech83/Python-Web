from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views import generic as auth_views

from petstagram.pets.models import Pet


class AddPetView(auth_views.CreateView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    fields = '__all__'


class DeletePetView(auth_views.DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'


class DetailsPetView(auth_views.DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        username = self.kwargs.get('username')
        pet_slug = self.kwargs.get('pet_slug')

        user = get_object_or_404(User, username=username)
        pet = get_object_or_404(Pet, slug=pet_slug)

        return pet


class EditPetView(auth_views.UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    fields = '__all__'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        username = self.kwargs.get('username')
        pet_slug = self.kwargs.get('pet_slug')

        user = get_object_or_404(User, username=username)
        pet = get_object_or_404(Pet, slug=pet_slug)

        return pet
