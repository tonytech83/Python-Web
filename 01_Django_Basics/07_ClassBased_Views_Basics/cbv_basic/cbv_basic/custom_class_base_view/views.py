from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("This is from Function-Base View")


# Custom CBV
class BaseView:
    @classmethod
    def as_view(cls):
        def view(request, *args, **kwargs):
            self = cls()

            # below is `dispatch` logic
            if request.method == "GET":
                return self.get(request, *args, **kwargs)
            else:
                return self.post(request, *args, **kwargs)

        return view


class IndexView(BaseView):
    def get(self, request):
        return HttpResponse("This is from Class-Base View")
