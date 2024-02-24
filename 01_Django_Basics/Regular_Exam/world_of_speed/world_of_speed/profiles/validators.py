import re

from django.core.exceptions import ValidationError


def username_validator(value):
    if not re.match(r'^\w+$', value):
        raise ValidationError('Username must contain only letters, digits, and underscores!')
