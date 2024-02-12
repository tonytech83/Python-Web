from django.urls import path

from cbv_advanced.web.views import CreateTodoView, ListTodoView

urlpatterns = (
    path('', ListTodoView.as_view(), name='todos-list'),

    path('create/', CreateTodoView.as_view(), name='todo-create'),
)
