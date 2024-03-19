from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_advanced.api.serializers import AuthorForListSerializer
from rest_advanced.web.models import Author


@api_view(http_method_names=['GET'])
def api_list_authors(request):
    authors_list = Author.objects.all()

    serializer = AuthorForListSerializer(authors_list, many=True)

    return Response(data=serializer.data)
