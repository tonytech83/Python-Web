from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

UserModel = get_user_model()


class Pet(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_URL_LENGTH = 300

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    pet_photo = models.URLField(
        max_length=MAX_URL_LENGTH,
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        # Call `super().save(*args, **kwargs)`, if not the pk will be 'None`
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk} - {self.name}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
