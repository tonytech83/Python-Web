from django.urls import path

from cbv_advanced.web.views import CreateTodoView, ListTodoView, DetailTodoView

urlpatterns = (
    path('', ListTodoView.as_view(), name='todos-list'),

    path('create/', CreateTodoView.as_view(), name='todo-create'),
    path('detail/<int:pk>/', DetailTodoView.as_view(), name='todo-detail'),
)
