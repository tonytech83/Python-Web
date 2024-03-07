from django.urls import path

from custom_auth.accounts.views import LoginUserView, RegisterUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login-user'),
    path('register/', RegisterUserView.as_view(), name='register-user'),
)
