from rest_framework import generics as api_views, permissions

from todos_app.todos.models import Todo, Category, TodoState
from todos_app.todos.serializers import CategorySerializer, TodoListSerializer, TodoCreateSerializer, \
    TodoDetailSerializer


class TodoListCreateApiView(api_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    list_serializer_class = TodoListSerializer
    create_serializer_class = TodoCreateSerializer
    serializer_class = list_serializer_class

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.create_serializer_class

        return self.list_serializer_class

    # Filter
    filter_funcs = [
        'filter_by_user',
        'filter_by_category',
        'filter_by_state',
    ]

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        for filter_func_name in self.filter_funcs:
            filter_func = getattr(self, filter_func_name, None)
            if filter_func:
                queryset = filter_func(queryset)

        return queryset

    def filter_by_user(self, queryset):
        return queryset.filter(user=self.request.user)

    def filter_by_category(self, queryset):
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def filter_by_state(self, queryset):
        state = self.request.query_params.get('state', None)
        if state is not None:
            expected_state = TodoState.DONE if state == 'true' else TodoState.NOT_DONE
            queryset = queryset.filter(state=expected_state)

        return queryset


class TodoDetailsUpdateApiView(api_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer

    def get_serializer(self, instance, data=None, partial=None):
        if self.request.method == 'PUT':
            data = {
                **data,
                'state': TodoState.DONE if data['is_done'] else TodoState.NOT_DONE,
            }

            return super().get_serializer(instance, data=data, partial=partial)

        return super().get_serializer(instance)


class CategoryListApiView(api_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
