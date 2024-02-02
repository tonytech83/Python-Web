from django.http import HttpResponse
from django.shortcuts import render

from django_intro.tasks.models import Task

"""
Function Base View

1. A function that has one or more params
2. Returns a response
"""


# def index(request):
#     name = request.GET.get('name', "NONAME")
#
#     content = '<h1>It works!</h1>' + f'<p>You are wellcome, {name}!</p>' + '<ul><li>1</li><li>2</li></ul>'
#
#     return HttpResponse(
#         content,
#
#         # we can change the content type, by default the 'Content-Type' is `text/html`
#         # headers={
#         #     'Content-Type': 'application/json',
#         # }
#     )

# def index(request):
#     # Search without `Form`
#     # can be used from address bar `http://127.0.0.1:8000/?filter=`
#     # after filter we past title of task
#     title_filter = request.GET.get('title_filter', None)
#
#     tasks = Task.objects.all()
#
#     if title_filter:
#         tasks = tasks.filter(title__icontains=title_filter.lower())
#
#     if not tasks:
#         return HttpResponse('<h1>No tasks found!!!</h1>')
#
#     result = []
#     [result.append(
#         f"""
#         <li>
#         <h2>{t.title}</h2>
#         <p>{t.description}</p>
#         </li>
#         """
#     ) for t in tasks]
#
#     ul = f'<ul>{"".join(result)}</ul>'
#
#     content = f"""
#     <h1>{len(tasks)}Tasks</h1>
#     {ul}
#     """
#
#     return HttpResponse(content)

def index(request):

    # This is only to show middleware
    print('In the view')

    title_filter = request.GET.get('title_filter', '')
    tasks = Task.objects.all()

    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter.lower())

    content = {
        'title': 'Task application',
        'message': 'You should HODL your Bitcoin!',
        'tasks': tasks,
        'tasks_count': tasks.count(),
        'title_filter': title_filter,
    }

    return render(request, 'tasks/index.html', content)
