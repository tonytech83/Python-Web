from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo
from petstagram.photos.utils import get_user_liked_photos


def details_photo(request, pk):
    photo = (Photo.objects
             .filter(pk=pk)
             .get())

    context = {
        'photo': photo,
        'has_user_liked_photo': get_user_liked_photos(pk),
        'likes_count': photo.photolike_set.count(),
    }

    return render(request, 'photos/photo-details-page.html', context)


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)

        if form.is_valid():
            # `form.save()` returns the saved instance of `Photo`
            photo = form.save()

            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()

            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
        'pk': photo.pk,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PhotoDeleteForm(instance=photo)
    else:
        form = PhotoDeleteForm(request.POST, instance=photo)

        if form.is_valid():
            form.save()

            return redirect('details user', pk=1)  # TODO: fix the pk when auth

    context = {
        'form': form,
        'pk': photo.pk,
    }

    return render(request, 'photos/photo-delete-page.html', context)
