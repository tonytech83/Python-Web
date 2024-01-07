from enum import Enum


class ChoicesEnumMixin(Enum):
    """
    Mixin for enum choises
    """

    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)
