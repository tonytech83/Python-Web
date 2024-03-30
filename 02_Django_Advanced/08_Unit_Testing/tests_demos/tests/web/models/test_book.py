# from unittest import TestCase
from django.core.exceptions import ValidationError
from django.test import TestCase

from tests_demos.web.models import Author, Book


class TestBook(TestCase):
    # Act__Arrange_Assert
    def test_book_crate__when_title_starts_with_uppercase__expect_to_be_created(self):
        # Arrange
        title = 'The book'
        author = Author.objects.create(name='The author')

        # Act
        book = Book.objects.create(title=title, author=author)
        book.full_clean()

        # Assert
        self.assertIsNotNone(book)

    def test_book_crate__when_title_starts_with_lowercase__expect_validation_error(self):
        # Arrange
        title = 'the book'
        author = Author.objects.create(name='The author')

        with self.assertRaises(ValidationError) as context:
            book = Book.objects.create(title=title, author=author)
            book.full_clean()

        self.assertEqual(['Book title must start with an capital letter.'], context.exception.messages)
