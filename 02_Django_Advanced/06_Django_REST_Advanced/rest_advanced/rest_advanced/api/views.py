from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics as api_generic_views, permissions

from rest_advanced.api.permissions import IsOwnerPermission
from rest_advanced.api.serializers import AuthorForListSerializer, BookForListSerializer, BookForCreateSerializer
from rest_advanced.web.models import Author, Book


@api_view(http_method_names=['GET'])
def api_list_authors(request):
    authors_list = Author.objects.all()

    serializer = AuthorForListSerializer(authors_list, many=True)

    return Response(data=serializer.data)


"""
Generic API Views:
1. ListAPIView - Retrieves a list of objects from DB
2. RetrieveAPIView - Retrieves a single object by its primary key
3. CreateAPIView - Creates a new object
4. UpdateAPIView - Updates an existing object by its primary key
5. DestroyAPIView - Deletes an existing object by its primary key
6. ListCreateAPIView - Combines list and create functionalities into single view
7. RetrieveUpdateAPIView - Combines retrieve and update functionalities into single view
8. RetrieveDestroyAPIView - Combines retrieve and destroy functionalities into single view
9. RetrieveUpdateDestroyAPIView - Combines retrieve, update and destroy functionalities into single view
"""


# 1
class BookListCreateApiView(api_generic_views.ListCreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerPermission,
    ]

    # # Permissions - the hard way
    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [permissions.IsAuthenticated()]

    # Serializer for list
    list_serializer_class = BookForListSerializer
    # Serializer for create
    create_serializer_class = BookForCreateSerializer

    # Set default serializer
    serializer_class = list_serializer_class

    # Change the serializer according to method
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.create_serializer_class

        return self.list_serializer_class

    # # Filter - not need to filter this way
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     # all params from url comes in `self.request.query_params`
    #     title_pattern = self.request.query_params.get('title')
    #
    #     # apply filter
    #     if title_pattern:
    #         queryset = queryset.filter(title__icontains=title_pattern)
    #
    #     return queryset

    # Filter
    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        title_pattern = self.request.query_params.get('title')

        # apply filter
        if title_pattern:
            queryset = queryset.filter(title__icontains=title_pattern)

        return queryset
