from django.urls import path

from todos_app.todos.views import TodoListCreateApiView, CategoryListApiView, TodoDetailsUpdateApiView

urlpatterns = (
    path('', TodoListCreateApiView.as_view(), name='api_todo_list_create'),
    path('<int:pk>/', TodoDetailsUpdateApiView.as_view(), name='api_todo_details'),
    path('categories/', CategoryListApiView.as_view(), name='api_category_list'),

)
