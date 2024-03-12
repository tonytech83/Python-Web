import time

from django.shortcuts import render
from django.views import generic as views

"""
Example without middleware with overwrite `dispatch()` method
"""


class IndexView(views.TemplateView):
    def dispatch(self, request, *args, **kwargs):
        # Code before the request

        dispatch_result = super().dispatch(request, *args, **kwargs)

        # Code after the request

        return dispatch_result


"""
Example without middleware with overwrite `dispatch()` method but in mixin
"""


class MeasureExecutionTimeMixin:
    def dispatch(self, request, *args, **kwargs):
        # Code before the request
        start_time = time.time()

        dispatch_result = super().dispatch(request, *args, **kwargs)

        # Code after the request
        end_time = time.time()

        print(f'Executed in {end_time - start_time} seconds')

        return dispatch_result


class Index2View(MeasureExecutionTimeMixin, views.TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        time.sleep(5)

        return super().get_context_data(**kwargs)
