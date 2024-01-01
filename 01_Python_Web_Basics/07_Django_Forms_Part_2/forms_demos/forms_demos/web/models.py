from django.db import models

from forms_demos.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_NAME_LENGTH = 20

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    # to work with media files, we should install pillow
    profile_image = models.ImageField(
        # where to be saved media files
        upload_to='persons',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_TODO_COUNT_PER_PERSON = 3
    MAX_TEXT_LENGTH = 25

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    assignee = models.ForeignKey(
        to=Person,
        on_delete=models.RESTRICT,
    )
