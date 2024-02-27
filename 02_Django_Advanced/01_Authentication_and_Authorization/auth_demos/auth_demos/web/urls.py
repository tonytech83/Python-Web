from django.urls import path

from auth_demos.web.views import LoginView, index, private_view

urlpatterns = (
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('private/', private_view, name='private_view'),
)
