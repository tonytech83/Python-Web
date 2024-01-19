import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

# Better to use `UserModel` to take `User` instead of `from django.contrib.auth.models import User`
UserModel = get_user_model()


# using `@login_required` decorator we prevent `AnonymousUser` login
@login_required
def index(request):
    suffix = random.randint(1, 1000)

    # Wrong way to create regular user, in this case password will be stored into database as plain-text
    # we can not authenticate the user with this password
    # UserModel.objects.create(
    #     username=f'TEST_{suffix}',
    #     password='Test_123456'
    # )

    # Proper way to create regular user - `create_user` method has function `make_password` which
    # turn a plain-text password into a hash for database storage
    UserModel.objects.create_user(
        username=f'TEST_{suffix}',
        password='Test_123456'
    )

    print(f'user login: {request.user}')

    user = UserModel.objects.get(username='admin')

    context = {
        'user': request.user,
        'permission': request.user.has_perm('auth.view_user')
    }

    return render(request, 'index.html', context)


# Class Base View example
# In CBV we prevent `AnonymousUser` login with mixin `LoginRequiredMixin`
class IndexView(views.TemplateView, LoginRequiredMixin):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pass


def login_user(request):
    # Authentication - `authenticate()` takes provided credentials and trying ot authenticate the user
    user = authenticate(
        username=f'TEST_301',
        password='Test_123456'
    )

    # Authorization - Does `request.user = user` and other stuff
    login(request, user)

    print(f'Logged in user: {user}')

    return redirect('index')


def logout_user(request):
    logout(request)

    return redirect('index')
