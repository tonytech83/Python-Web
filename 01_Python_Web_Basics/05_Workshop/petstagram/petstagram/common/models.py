# common/models.py

from django.db import models

from petstagram.photos.models import Photo


class PhotoComment(models.Model):
    MAX_COMMENT_LENGTH = 300

    text = models.CharField(
        max_length=MAX_COMMENT_LENGTH,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    # Photo's filed for likes is named `{NAME_OF_THE_MODEL}_set`
    photo = models.ForeignKey(
        to=Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )
