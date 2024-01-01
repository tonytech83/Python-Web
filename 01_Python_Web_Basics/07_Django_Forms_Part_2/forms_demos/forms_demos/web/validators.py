from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

"""
Function validators - quick and simple, but for simple validations
"""


def validate_text(value):
    # if valid:
    #   do nothing
    # else:
    #   raise ValidationException()

    if '_' in value:
        raise ValidationError(
            message='`_` is invalid character for `text` field',
            code='invalid',
        )


def validate_priority(value):
    if value < 1 or 10 < value:
        raise ValidationError('Priority must be between 1 and 10')


"""
Class validators - for more complex validations
 - should have `__init__` and `__call__` for Form validation
 - should have also `__eq__`  and `@deconstructible` decorator when # using it in Model
"""


@deconstructible
class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValidationError(f'Priority must be between {self.min_value} and {self.max_value}')

    def __eq__(self, other):
        return (
                isinstance(other, self.__class__)
                and self.min_value == other.min_value
                and self.max_value == other.max_value
        )
