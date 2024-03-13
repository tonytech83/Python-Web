import time

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


"""
Example for Django session

This should be done in `dispatch` or `get`
"""


def get_load_count(request):
    load_count = request.session.get('load_count', 0)

    return load_count + 1


class Index3View(views.TemplateView):
    template_name = 'web/index-session.html'

    def dispatch(self, request, *args, **kwargs):
        load_count = get_load_count(request)
        request.session['load_count'] = load_count

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        time.sleep(1)
        context = super().get_context_data(**kwargs)
        context['load_count'] = self.request.session.get('load_count', 0)
        return context
