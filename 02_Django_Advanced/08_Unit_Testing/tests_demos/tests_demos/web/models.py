from django.db import models

from tests_demos.web.validators import validate_book_title


# This model no need to be tested, because there no any custom logic
class Author(models.Model):
    MAX_NAME_LENGTH = 50

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )


class Genre(models.TextChoices):
    FANTASY = "Fantasy", "Fantasy"
    HORROR = "Horror", "Horror"
    ACTION = "Action", "Action"
    COMEDY = "Comedy", "Comedy"
    ROMANCE = "Romance", "Romance"
    ADVENTURE = "Adventure", "Adventure"
    THRILLER = "Thriller", "Thriller"


class Book(models.Model):
    MAX_TITLE_LENGTH = 100

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        # This custom validators should be tested
        validators=(
            validate_book_title,
        ),
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=max(len(g) for _, g in Genre.choices),
        choices=Genre.choices,
        default=Genre.FANTASY,
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

    # This custom code should be tested
    def __str__(self):
        return f'{self.title} by {self.author}'
