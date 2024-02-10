import datetime

from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render

from cbv_basic.web.models import Todo


# Function-Base Views
def index(request):
    if request.method == 'GET':
        # perform GET logic
        pass
    else:
        # perform POST logic
        pass

    # Do something

    context = {

    }

    return render(request, 'web/index.html', context)


# Class-Base Views
# - views.View - Base functionality
class IndexRawView(views.View):
    def dispatch(self, request, *args, **kwargs):
        # in `dispatch` executed code before current view

        # for example: check user permissions
        # if random() < 0.5:
        #     return HttpResponseNotAllowed(['GET'])

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # perform GET logic
        return render(request, 'web/index.html')

    def post(self, request):
        # perform POST logic
        pass


# - views.TemplateView
class IndexView(views.TemplateView):
    template_name = 'web/index.html'  # minimum for TemplateView

    # `context` with static data, i.e. no BD calls
    extra_context = {
        'title': 'This comes form `extra_context`',
        'static_time': datetime.datetime.now(),
    }

    # overwriting `get_context_data` to have `context` with dynamic data (DB calls)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.datetime.now()
        context['todo_list'] = Todo.objects.all()

        return context


# Generic Editing Views for Forms
# - CreateView
class TodoCreateView(views.CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'web/create_todo.html'

    # Static way
    # success_url = reverse_lazy('template-view-index')

    # Dynamic way - use it if we want to display object after creation
    def get_success_url(self):
        # after creation success_url is dynamic and sent to "details-todo" with pk of the created todo
        return reverse('details-todo', kwargs={'pk': self.object.pk})

    # Static way to chose form
    # form_class = TodoBaseForm

    # Dynamic way
    def get_form_class(self):
        # return TodoBaseForm - if we want to return our Form with more customizations
        return super().get_form_class()

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        # used for small customizations
        form.fields['deadline'].widget.attrs['type'] = 'date'
        form.fields['deadline'].widget.attrs['class'] = 'form-control'

        return form

# - UpdateView


# - DetailsView
class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = 'web/details_todo.html'
