from django.urls import path

from users_demos.accounts.views import LoginUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login-user'),
)
