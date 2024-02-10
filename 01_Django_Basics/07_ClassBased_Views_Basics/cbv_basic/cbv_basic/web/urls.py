from django.urls import path

from cbv_basic.web.views import index, IndexRawView, IndexView, TodoCreateView, TodoDetailsView, TodoListView

urlpatterns = (
    path('', IndexView.as_view(), name='template-view-index'),

    path('todos/create/', TodoCreateView.as_view(), name='create-todo'),
    path('todos/<int:pk>', TodoDetailsView.as_view(), name='details-todo'),
    path('todos/', TodoListView.as_view(), name='list-todos'),

    path('raw/', IndexRawView.as_view(), name='row-index'),
    path('raw/<int:pk>/', IndexRawView.as_view(), name='row-index-with-pk'),
)
