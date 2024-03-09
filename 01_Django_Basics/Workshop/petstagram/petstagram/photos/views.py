from django.urls import reverse
from django.views import generic as views

from django.contrib.auth import mixins as auth_mixins

from petstagram.core.view_mixins import OwnerRequiredMixin
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


class AddPhotoView(OwnerRequiredMixin, views.CreateView):
    queryset = (Photo.objects.all()
                .prefetch_related('tagged_pets'))

    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'

    def get_success_url(self):
        return reverse('photos:photo-list', kwargs={
            'pk': self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user

        return form


class DetailPhotoView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = (Photo.objects.all()
                .prefetch_related('photolike_set')
                .prefetch_related('photocomment_set')
                .prefetch_related('tagged_pets'))

    template_name = 'photos/photo-details-page.html'


class EditPhotoView(OwnerRequiredMixin, views.UpdateView):
    queryset = (Photo.objects.all()
                .prefetch_related('tagged_pets'))

    template_name = 'photos/photo-edit-page.html'
    form_class = PhotoEditForm

    def get_success_url(self):
        return reverse("detail-photo", kwargs={
            "pk": self.object.pk,
        })
