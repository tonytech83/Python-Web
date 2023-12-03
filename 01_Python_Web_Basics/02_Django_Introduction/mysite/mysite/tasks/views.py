from django.shortcuts import render

from mysite.tasks.models import Task


def index(request):
    tasks_list = Task.objects.all()

    context = {
        'tasks': tasks_list
    }

    return render(request, 'index.html', context)
