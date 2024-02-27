from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import render

from auth_demos.web.models import Model1


class LoginView(auth_views.LoginView):
    pass


def index(request):
    # `param` comes form request for example
    param = '1'

    # Not possible SQL injection
    model1_list_ = Model1.objects.all().filter(pk=param)

    # Possible SQL injections
    model1_list2 = Model1.objects.raw(
        f"SELECT * FROM web_model1 WHERE id={param}",
    )

    # Not possible SQL injection
    model1_list3 = Model1.objects.raw(
        "SELECT * FROM web_model1 WHERE id=%s",
        [param]
    )

    context = {
        'model1_list': Model1.objects.all(),
    }

    return render(request, 'index.html', context)


# There should also decorator or mixin on View (func or class)
def private_view(request):
    return HttpResponse("View Accessed")
