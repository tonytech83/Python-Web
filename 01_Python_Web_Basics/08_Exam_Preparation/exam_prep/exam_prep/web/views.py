from django.shortcuts import render

"""
•	http://localhost:8000/ - home page
•	http://localhost:8000/album/add/ - add album page
•	http://localhost:8000/album/details/<id>/ - album details page
•	http://localhost:8000/album/edit/<id>/ - edit album page
•	http://localhost:8000/album/delete/<id>/ - delete album page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/delete/ - delete profile page
"""


def index(request):
    return render(request, 'core/home-no-profile.html')


def add_album(request):
    if request.method == 'GET':
        ...
    else:
        ...

    context = {

    }

    return render(request, 'albums/add-album.html', context)


def details_album(request, pk):
    return render(request, 'albums/album-details.html')


def edit_album(request, pk):
    return render(request, 'albums/edit-album.html')


def delete_album(request, pk):
    return render(request, 'albums/delete-album.html')


def details_profile(request):
    return render(request, 'profiles/profile-details.html')


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')
