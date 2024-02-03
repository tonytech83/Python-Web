from django.urls import path, include

from urls_and_views.core.views import index, index_json, index_html, redirect_to_softuni, redirect_to_index, \
    redirect_to_index_with_params, raise_error, raise_exception

urlpatterns = (
    # Redirects
    path('to-softuni/', redirect_to_softuni, name='softuni-redirect'),
    path('to-index/', redirect_to_index, name='index-redirect'),
    path('to-index-wiht-params/', redirect_to_index_with_params, name='redirect_to_index_with_params'),

    # Errors
    path('raise-error', raise_error, name='raise_error'),
    path('raise-exception', raise_exception, name='raise_exception'),

    # Normal URLs
    path('', index, name='index'),
    path('<int:pk>/', index, name='index-pk'),
    path('<slug:slug>/', index, name='index-slug'),
    path('<int:pk>/<slug:slug>/', index, name='index-pk-slug'),

    path('json/', include([
        path('<int:pk>/', index_json, name='json-index-pk'),
        path('<slug:slug>/', index_json, name='json-index-slug'),
        path('<int:pk>/<slug:slug>/', index_json, name='json-index-pk-slug'),
    ])),

    path('html/', include([
        path('', index_html, name='html-index'),
    ])),
)
