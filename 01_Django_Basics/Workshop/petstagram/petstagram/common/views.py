from django.shortcuts import render, redirect
from django.views import generic as auth_views

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


class HomePageView(auth_views.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pet_photos'] = Photo.objects.all()

        return context


def like_pet_photo(request, pk):
    pet_photo_like = (PhotoLike.objects
                      .filter(to_photo_id=pk)
                      .first())

    if pet_photo_like:
        # dislike
        pet_photo_like.delete()
    else:
        # like
        PhotoLike.objects.create(to_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")
