from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_list_or_404, redirect

"""
In FBV args are not using
"""


def index(request, *args, **kwargs):
    content = (f"<h1>It works with:</h1><br>"
               f"<strong>args</strong> = {args} and <strong>kwargs</strong> = {kwargs},<br>"
               f"<strong>form path</strong> -> '{request.path}',<br>"
               f"<strong>method</strong> -> '{request.method}',<br>"
               f"<strong>and user</strong> -> '{request.user}',")

    return HttpResponse(
        content,
        # status=201,
    )


def index_json(request, *args, **kwargs):
    json_data = (
        {
            'args': args,
            'kwargs': kwargs,
            'path': request.path,
            'method': request.method,
            'user': str(request.user),
        }
    )

    return JsonResponse(
        json_data,
        # content_type="application/json",
        safe=False,
    )


# render and content
def index_html(request, *args, **kwargs):
    users_list = get_list_or_404(User.objects.all())

    context = {
        'title': 'Request data',
        'args': args,
        'kwargs': kwargs,
        'path': request.path,
        'method': request.method,
        'user': request.user,
    }

    return render(request, 'core/index.html', context)


# redirect to absolute URL
def redirect_to_softuni(request):
    return redirect('https://softuni.bg/')


# redirect to abstract URL
def redirect_to_index(request):
    return redirect('index')


# redirect to abstract URL with parameters
def redirect_to_index_with_params(request):
    return redirect('index-pk-slug', pk=41, slug='test-slug')


# Raise error
def raise_error(request):
    return HttpResponseNotFound()


# Raise exception
# To work:
# 1. Change DEBUG in `settings.py` to False
# 2. Change `ALLOWED_HOSTS = []` in `settings.py` to `ALLOWED_HOSTS = ['*']`
# 3. Create `404.html` into `templates`
def raise_exception(request):
    raise Http404
