from rest_framework import serializers

from rest_advanced.web.models import Book, Author


class AuthorForBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class AuthorForCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookForAuthorListListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# This is for List
class BookForListSerializer(serializers.ModelSerializer):
    # Nested Serializer
    author = AuthorForBookListSerializer(many=False)

    class Meta:
        model = Book
        fields = '__all__'


# This is for create
class BookForCreateSerializer(serializers.ModelSerializer):
    author = AuthorForCreateSerializer(many=False)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        # `validated_data` in DRF is the same as `cleaned_data` in Django Forms
        author_data = self.validated_data.pop('author', None)
        # author validation

        # Check if `author` exists or create
        author, _ = Author.objects.get_or_create(**author_data)

        # Rewrite information for `author`
        book_data = {
            **self.validated_data,
            'author': author,
        }

        return Book.objects.create(**book_data)


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
