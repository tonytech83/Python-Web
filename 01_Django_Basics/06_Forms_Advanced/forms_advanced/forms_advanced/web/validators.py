"""
Django wants a callable with a single arg that raise a ValidationError if data is invalid.
Validators can be used in Models and Forms
"""
from django.core.exceptions import ValidationError


def validate_email(email):
    if '@' not in email:
        raise ValidationError('Email must contains `@` character')


class FileSizeValidator:
    def __init__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        if value.size > self.max_file_size:
            raise ValidationError(f'The file size must be less than {self.max_file_size}')


file = ...  # some file

validate_email('test@test.com')
FileSizeValidator(max_file_size=5)(file)
