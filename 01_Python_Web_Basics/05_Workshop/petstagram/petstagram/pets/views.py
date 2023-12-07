from django.shortcuts import render


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def details_details(request, pk):
    return render(request, 'pets/pet-details-page.html')


def edit_pet(request, pk):
    return render(request, 'pets/pet-edit-page.html')


def delete_pet(request, pk):
    return render(request, 'pets/pet-delete-page.html')
