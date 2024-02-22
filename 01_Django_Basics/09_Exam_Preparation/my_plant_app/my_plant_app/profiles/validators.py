from django.core.exceptions import ValidationError


def validate_first_letter_capitalized(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")
