from django.core.exceptions import ValidationError


def validate_book_title(book_title):
    if not book_title[0].isupper():
        raise ValidationError("Book title must start with an capital letter.")
