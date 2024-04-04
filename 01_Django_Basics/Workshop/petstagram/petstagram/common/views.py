from django.shortcuts import redirect
from django.views import generic as views

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


class HomePageView(views.ListView):
    queryset = (Photo.objects.all()
                .prefetch_related('tagged_pets')
                .prefetch_related('photolike_set')
                .prefetch_related('photocomment_set')
                .order_by('-date_of_publication'))

    template_name = 'common/home-page.html'

    paginate_by = 1

    @property
    def pet_name_pattern(self):
        return self.request.GET.get('pet_name_pattern', None)

    # Search 1
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = self._filter_by_pet_name_pattern(queryset)

        return queryset

    def _filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        filter_query = {}

        # can be used if we want to search by many parameters
        if pet_name_pattern:
            filter_query['tagged_pets__name__icontains'] = pet_name_pattern

        return queryset.filter(**filter_query)

    # if we want to have searched pattern in input field after click Search button
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pet_name_pattern'] = self.pet_name_pattern or ''

        return context

    # Search 2
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     pet_name_pattern = self.request.GET.get('pet_name_pattern', None)
    #
    #     context['pet_photos'] = Photo.objects.all()
    #
    #     if pet_name_pattern:
    #         context['pet_name_pattern'] = pet_name_pattern
    #         context['pet_photos'] = context['pet_photos'].filter(tagged_pets__name__icontains=pet_name_pattern)
    #
    #     return context


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
