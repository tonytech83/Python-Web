from django.views import generic as auth_views

from petstagram.photos.models import Photo


class AddPhotoView(auth_views.CreateView):
    model = Photo
    template_name = 'photos/photo-add-page.html'


class DetailPhotoView(auth_views.DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'


class EditPhotoView(auth_views.UpdateView):
    model = Photo
    template_name = 'photos/photo-edit-page.html'
