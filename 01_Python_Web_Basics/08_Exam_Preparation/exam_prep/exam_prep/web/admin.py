from django.contrib import admin

from exam_prep.web.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'age',
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'genre',
        'price',
    )
