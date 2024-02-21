from django.urls import reverse_lazy
from django.views import generic as views

from my_music_app.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from my_music_app.albums.models import Album
from my_music_app.profiles.models import Profile


class AlbumCreateView(views.CreateView):
    form_class = AlbumCreateForm
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()

        return super().form_valid(form)


class AlbumDetailsView(views.DetailView):
    queryset = Album.objects.all()
    template_name = 'album/album-details.html'


class AlbumEditView(views.UpdateView):
    queryset = Album.objects.all()
    template_name = 'album/album-edit.html'
    form_class = AlbumEditForm

    success_url = reverse_lazy('home-page')


class AlbumDeleteView(views.DeleteView):
    queryset = Album.objects.all()
    template_name = 'album/album-delete.html'
    form_class = AlbumDeleteForm

    success_url = reverse_lazy('home-page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object

        return kwargs

