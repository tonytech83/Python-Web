from petstagram.pets.models import Pet


def get_pet_by_name_and_username(pet_slug, username):
    # TODO: when has auth

    return Pet.objects.get(slug=pet_slug)
