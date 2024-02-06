from django.urls import path

from forms_basic.web.views import index, index_modelform, update_employee

urlpatterns = (
    path('', index, name='index'),
    path('model-form/', index_modelform, name='model-form'),
    path('model-form/<int:pk>/', update_employee, name='update-employee'),
)
