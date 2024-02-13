from django import forms

from django.urls import reverse_lazy
from django.views import generic as views


from cbv_advanced.web.models import Todo

"""
Generic Views in Django are 5:
    - Create -> CreateView
    - Read -> DetailView & ListView
    - Update -> UpdateView
    - Delete -> DeleteView
"""


# Create View
class CreateTodoView(views.CreateView):
    # Minimum
    model = Todo  # or queryset = Todo.objects.all()
    fields = ['title', 'description']  # or `exclude` or `form_class`

    template_name = 'web/create_todo.html'  # optional, but it is good to be used
    success_url = reverse_lazy('todos-list')  # optional, but it is good to be used. Ather option is from Model


# Example for filter with Form
class FilterTodoForm(forms.Form):
    title_pattern = forms.CharField(
        max_length=Todo.MAX_TITLE_LENGTH,
        required=False,
    )

    is_done = forms.BooleanField(
        required=False,
    )


# ListView
class ListTodoView(views.ListView):
    # Minimum
    model = Todo
    template_name = 'web/list_todo.html'

    # Pagination - Static way
    paginate_by = 3

    # Overwrites:
    # - add additional variable in context
    # - add Form in context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Todos list:'
        context['filter_form'] = FilterTodoForm(
            initial={
                'title_pattern': self.request.GET.get('title_pattern')
            }
        )

        # Not a good idea
        # context['object_list'] = context['object_list'].filter(title__icontains='clean')

        return context

    # - made filtration
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = self.apply_filter(queryset)

        # hardcoded filter
        # queryset = queryset.filter(title__icontains='clean')

        return queryset

    def apply_filter(self, queryset):
        title_pattern = self._get_title_pattern()
        if title_pattern:
            queryset = queryset.filter(title__icontains=title_pattern)

        is_done = self._get_is_done_filter()
        if is_done is not None:
            queryset = queryset.filter(is_done=is_done)

        return queryset

    # Additional func to take `title_pattern` and `is_done`
    def _get_title_pattern(self):
        return self.request.GET.get('title_pattern', None)

    def _get_is_done_filter(self):
        return self.request.GET.get('is_done', None) == 'on'

    # Paginator - Dynamic way / needs js
    # def get_paginate_by(self, queryset=None):
    #     pass


# Detail View
class DetailTodoView(views.DetailView):
    # Minimum
    model = Todo
    template_name = 'web/detail_todo.html'

    # Optional
    slug_field = 'slug'
    query_pk_and_slug = True  # takes with both `pk` and `slug`

    # Overwrites:
    # - additional filter before filter by slug, because slug can be not unique
    def get_queryset(self):
        queryset = super().get_queryset()

        tenant = self.request.GET.get('tenant', None)
        if tenant is not None:
            queryset = queryset.filter(tenant=tenant)

        return queryset
