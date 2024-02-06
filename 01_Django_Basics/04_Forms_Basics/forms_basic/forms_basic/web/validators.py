from django.core.exceptions import ValidationError


def non_empty_spaces(value):
    if ' ' in value:
        raise ValidationError('Whitespaces are not allowed')
