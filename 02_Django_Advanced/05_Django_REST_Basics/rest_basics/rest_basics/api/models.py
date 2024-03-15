from django.db import models


class Genre(models.TextChoices):
    FANTASY = 'Fantasy'
    SCI_FI = 'Sci-Fi'


class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField(default=0)
    description = models.TextField(max_length=100, default='')
    author = models.CharField(max_length=20)
    genre = models.CharField(
        max_length=max(len(genre[1]) for genre in Genre.choices),
        choices=Genre.choices,
    )

    def __str__(self):
        return self.title
