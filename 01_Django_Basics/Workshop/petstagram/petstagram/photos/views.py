from django.shortcuts import render
from django.views import generic as auth_views

from petstagram.photos.models import Photo


class AddPhotoView(auth_views.CreateView):
    model = Photo
    template_name = 'photos/photo-add-page.html'
    fields = '__all__'


# class DetailPhotoView(auth_views.DetailView):
#     model = Photo
#     template_name = 'photos/photo-details-page.html'

def detail_photo(request, pk):
    context = {
        'pet_photo': Photo.objects.get(pk=pk),
    }

    return render(request, 'photos/photo-details-page.html', context)


class EditPhotoView(auth_views.UpdateView):
    model = Photo
    template_name = 'photos/photo-edit-page.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pet_photo'] = self.object

        return context
