from django.shortcuts import render, redirect, resolve_url

from petstagram.common.models import PhotoLike
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo

from petstagram.photos.models import Photo

import pyperclip

from petstagram.photos.utils import get_user_liked_photos, get_photo_url


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }

    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # # Variant 1
        # photo_like = PhotoLike(
        #     photo_id=photo_id,
        # )
        # photo_like.save()

        # Variant 2
        PhotoLike.objects.create(
            photo_id=photo_id,
        )

        # # Variant 3
        # # using only validation is needed (makes addition call to DB)
        # photo = Photo.objects.get(pk=photo_id)
        # PhotoLike.objects.create(
        #     photo=photo,
        # )

    # for example `get_photo_url()` will return: http://127.0.0.1:8000/#photo-1
    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    pyperclip.copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(get_photo_url(request, photo_id))
