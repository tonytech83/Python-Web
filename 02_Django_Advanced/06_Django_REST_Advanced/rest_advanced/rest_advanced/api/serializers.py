from rest_framework import serializers

from rest_advanced.web.models import Book, Author


class AuthorForBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookForAuthorListListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# This causing loop
class BookForListSerializer(serializers.ModelSerializer):
    # Nested Serializer
    author = AuthorForBookListSerializer(many=False, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


# This is OK, there no defined `author`
class BookForAuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForListSerializer(serializers.ModelSerializer):
    book_set = BookForAuthorListSerializer(many=True)

    class Meta:
        model = Author
        fields = ('name', 'book_set')
