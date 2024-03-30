from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

from django.contrib.auth import mixins as auth_mixins

UserModel = get_user_model()


def show_users(request):
    user_list = UserModel.objects.all()

    context = {
        'user_list': user_list,
    }

    return render(request, 'web/users.html', context)


# This code no need of testing
class ListUsersView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'web/users.html'

    # This is custom code and should be tested
    def get_queryset(self):
        queryset = UserModel.objects.all()
        queryset = queryset.order_by('-date_joined')

        return queryset
