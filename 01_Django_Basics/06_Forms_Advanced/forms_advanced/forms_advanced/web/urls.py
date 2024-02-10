from django.urls import path

from forms_advanced.web.views import index, create_person, show_formset, styling_demos, crispy_form

urlpatterns = (
    path('', index, name='index'),
    path('person/create/', create_person, name='create-person'),
    path('formsets/', show_formset, name='show-formset'),
    path('styling', styling_demos, name='styling-demos'),
    path('crispy/', crispy_form, name='crispy-form'),
)
