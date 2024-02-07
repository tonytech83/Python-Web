import random

from django.shortcuts import render

cats = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKywdss6chaqCALU-Cid3aWB-7xQFletKxIw&s',
    'https://twin-cities.umn.edu/sites/twin-cities.umn.edu/files/Pallas%27scat2.png'
]


def index(request):
    context = {
        'cat_image': random.choice(cats),
    }
    return render(request, 'web/index.html', context)


def about(request):
    return render(request, 'web/about.html')
