from django.urls import path

from departments_app.departments import views

urlpatterns = [
    path('department/<int:department_id>', views.show_department_by_id, name='details department'),
]
