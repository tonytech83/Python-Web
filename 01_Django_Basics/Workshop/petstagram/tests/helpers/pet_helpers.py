from petstagram.pets.models import Pet

PET_DATA = {
    'name': 'TestPet',
    'pet_photo': 'https://example.com/pet.jpg',
    'date_of_birth': '2020-10-01',
}


def create_valid_pet(user):
    pet = Pet(
        **PET_DATA,
        user=user,
    )

    pet.save()

    return pet
