from django.contrib import admin

from django_intro.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'done')
    list_filter = ('done',)
