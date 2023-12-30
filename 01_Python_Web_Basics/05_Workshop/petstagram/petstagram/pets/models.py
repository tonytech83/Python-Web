# pets/models.py


from django.db import models
from django.template.defaultfilters import slugify

from petstagram.core.model_mixins import StrFromFieldMixin

"""
The fields Name and Pet Photo are required:
•	Name - it should consist of a maximum of 30 characters.
•	Personal Pet Photo - the user can link a picture using a URL
The field date of birth is optional:
•	Date of Birth - pet's day, month, and year of birth
"""


class Pet(StrFromFieldMixin, models.Model):
    str_fields = ('name',)
    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        blank=False,
        null=False,
    )

    personal_photo = models.URLField(
        blank=False,
        null=False,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # With this approach we don't have auto generated `slug` before creation

        # Create/Update - to generate an id, because we will have 'none' for id
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        # Update
        return super().save(*args, **kwargs)
