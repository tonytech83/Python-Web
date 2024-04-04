from petstagram.photos.models import Photo

PHOTOS_DATA = {
    "photo": "photo.jpg",
    "description": "Test description",
    "location": "Sofia",
}


def create_valid_photo(user, pets):
    photo = Photo(
        **PHOTOS_DATA,
        user=user,
    )

    photo.save()
    photo.tagged_pets.add(pets)
    photo.save()

    return photo
