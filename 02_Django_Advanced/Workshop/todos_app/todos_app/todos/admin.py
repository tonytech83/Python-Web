from django.contrib import admin

from todos_app.todos.models import Todo, Category


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'state', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
