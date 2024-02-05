from django.db import models


class Employee(models.Model):
    MAX_LENGTH_NAME = 35

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=False,
        null=False,
    )
