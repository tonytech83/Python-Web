from django.contrib import admin

from mysite.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'task_text')
