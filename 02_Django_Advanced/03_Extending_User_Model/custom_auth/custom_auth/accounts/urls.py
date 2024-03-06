from django.urls import path

from custom_auth.accounts.views import LoginUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login-user'),
)
