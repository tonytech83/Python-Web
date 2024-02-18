from django.urls import reverse, reverse_lazy
from django.views import generic as views

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(views.CreateView):
    # when using CreateView `model` is not needed
    # model = Pet
    template_name = 'pets/pet-add-page.html'
    form_class = PetCreateForm

    def get_success_url(self):
        return reverse('details-pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug
        })


class EditPetView(views.UpdateView):
    model = Pet  # or queryset = Pet.objects.all()
    template_name = 'pets/pet-edit-page.html'
    form_class = PetEditForm

    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['username'] = 'admin'

        return context

    def get_success_url(self):
        return reverse('details-pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug
        })


class DetailsPetView(views.DetailView):
    # model = Pet  # or `queryset`

    # with `queryset` we can optimize the queries to DB
    queryset = (Pet.objects.all()
                .prefetch_related('photo_set')
                .prefetch_related('photo_set__tagged_pets'))

    template_name = 'pets/pet-details-page.html'

    slug_url_kwarg = 'pet_slug'  # name of param in URL

    # this code is replaced with `slug_url_kwarg = 'pet_slug'`
    # def get_object(self, queryset=None):
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #
    #     # username = self.kwargs.get('username')
    #     pet_slug = self.kwargs.get('pet_slug')
    #
    #     # user = get_object_or_404(User, username=username)
    #     pet = get_object_or_404(Pet, slug=pet_slug)
    #
    #     return pet


class DeletePetView(views.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('home-page')

    extra_context = {
        'username': 'admin',
    }

    # Both overwritten methods do same
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = self.form_class(instance=self.object)
    #
    #     return context
