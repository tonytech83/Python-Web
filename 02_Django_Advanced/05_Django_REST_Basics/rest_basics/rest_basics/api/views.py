from django.shortcuts import render, redirect

from django.views import generic as views
from rest_framework import views as api_views, status

from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_basics.api.models import Book


# Function view

def list_books(request):
    book_list = Book.objects.all()

    context = {'book_list': book_list}

    return render(request, '...', context)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


@api_view(http_method_names=['GET'])
def api_list_books(request):
    book_list = Book.objects.all()

    serializer = BookSerializer(book_list, many=True)

    json = serializer.data

    return Response(data=json)


# Class-Base view

class BookListView(views.View):
    def get(self, request):
        return render(request, "")

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('')

        return render(request, '', context=None)


class BookListApiView(api_views.APIView):
    def get(self, request):
        book_list = Book.objects.all()

        serializer = BookSerializer(book_list, many=True)

        json = serializer.data

        return Response(data=json)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookUpdateApiView(api_views.APIView):
    def get_object(self, pk):
        return Book.objects.filter(pk=pk).first()

    def get(self, request, pk):
        serializer = BookSerializer(instance=self.get_object(pk), many=False)

        json = serializer.data

        return Response(data=json)

    def put(self, request, pk):
        book = Book.objects.filter(pk=pk).first()

        serializer = BookSerializer(data=request.data, instance=self.get_object(pk))
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
