from django.urls import path

from forms_demos.web import views

urlpatterns = (
    path('', views.index, name='form'),
    path('model_form', views.index2, name='model form'),
    path('persons/', views.list_persons, name='list persons'),
    path('persons/create/', views.create_person, name='create person'),
)
