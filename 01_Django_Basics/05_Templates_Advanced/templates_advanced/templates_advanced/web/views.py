import random

from django.shortcuts import render

cat_images = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKywdss6chaqCALU-Cid3aWB-7xQFletKxIw&s',
    'https://twin-cities.umn.edu/sites/twin-cities.umn.edu/files/Pallas%27scat2.png'
]

cat_names = [
    'John',
    'Penka',
]


def index(request):
    idx = random.randint(0, len(cat_images) - 1)

    context = {
        'cat_image': cat_images[idx],
        'cat_name': cat_names[idx],
        'numbers': [x for x in range(-10, 11)],
    }

    return render(request, 'web/index.html', context)


def about(request):
    return render(request, 'web/about.html')


# Bootstrap examples view
def show_bootstrap(request):
    context = {
        'has_bootstrap': request.GET.get('has_bootstrap', False),
    }

    return render(request, 'web/bootstrap.html', context)
