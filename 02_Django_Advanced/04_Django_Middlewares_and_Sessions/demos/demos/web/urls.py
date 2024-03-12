from django.urls import path

from demos.web.views import Index2View

urlpatterns = (
    path('', Index2View.as_view(), name='index'),
)
