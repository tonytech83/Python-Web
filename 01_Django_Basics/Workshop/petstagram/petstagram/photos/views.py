from django.urls import reverse
from django.views import generic as views

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


class AddPhotoView(views.CreateView):
    queryset = (Photo.objects.all()
                .prefetch_related('tagged_pets'))

    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'

    def get_success_url(self):
        return reverse('photos:photo-list', kwargs={
            'pk': self.object.pk,
        })


class DetailPhotoView(views.DetailView):
    queryset = (Photo.objects.all()
                .prefetch_related('photolike_set')
                .prefetch_related('photocomment_set')
                .prefetch_related('tagged_pets'))

    template_name = 'photos/photo-details-page.html'


class EditPhotoView(views.UpdateView):
    queryset = (Photo.objects.all()
                .prefetch_related('tagged_pets'))

    template_name = 'photos/photo-edit-page.html'
    form_class = PhotoEditForm

    def get_success_url(self):
        return reverse("detail-photo", kwargs={
            "pk": self.object.pk,
        })
