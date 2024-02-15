from django.core.exceptions import ValidationError

from petstagram.core.utils import megabytes_to_bytes


def validate_file_size(image_object):
    max_image_size = 5

    if image_object.size > megabytes_to_bytes(max_image_size):
        raise ValidationError(f'The maximum file size that can be uploaded is {max_image_size}MB')
