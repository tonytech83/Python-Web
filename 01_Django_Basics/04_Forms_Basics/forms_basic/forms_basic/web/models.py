from django.db import models

from forms_basic.web.validators import non_empty_spaces


class Employee(models.Model):
    MAX_LENGTH_NAME = 35
    ROLES = (
        (1, 'Software Engineer'),
        (2, 'Developer'),
        (3, 'QA Engineer')
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=False,
        null=False,
        validators=(
            non_empty_spaces,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=False,
        null=False,
    )

    role = models.IntegerField(
        choices=ROLES,
        blank=False,
        null=False,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
