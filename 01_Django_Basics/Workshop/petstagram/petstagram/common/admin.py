from django.contrib import admin

from petstagram.common.models import PhotoComment


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_time_of_publication')
