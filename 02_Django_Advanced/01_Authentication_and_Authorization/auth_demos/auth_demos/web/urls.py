from django.urls import path

from auth_demos.web.views import LoginView

urlpatterns = (
    path('accounts/login/', LoginView.as_view(), name='login'),
)
