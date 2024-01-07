from django.core.exceptions import ValidationError
import re


def username_validator(value):
    pattern = r'^\w+$'

    if not bool(re.match(value, pattern)):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
