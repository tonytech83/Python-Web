from django.urls import path, include

from urls_and_views.departments.views import index, department_1_details, department_2_details, department_details, \
    department_details_by_name

urlpatterns = (
    path('', index, name='index'),

    # not a proper way to declare URLs
    # path('department/1/', department_1_details, name='department_1_details'),
    # path('department/2/', department_2_details, name='department_2_details'),

    # The arrangement should be int -> str -> regex
    # path('department/<int:pk>/', department_details, name='department-details'),
    # path('department/<str:name>/', department_details_by_name, name='department_by_name'),

    # same as above
    path('department/', include([
        path('<int:pk>/', department_details, name='department-details'),
        path('<str:name>/', department_details_by_name, name='department_by_name')
    ])),
)

"""
Diff between `path` and `str` in urls:

|                       | department/<str:name> | department/<str:name>/<str:fname> | department/<path:name>    |
| department/test/proba | Not match             | Match: name=test, fname=proba     | Match: `test/proba`       |
"""
