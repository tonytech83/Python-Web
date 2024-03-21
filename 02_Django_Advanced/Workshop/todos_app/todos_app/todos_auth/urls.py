from django.urls import path, include

from todos_app.todos_auth.views import CreateUserApiView, LoginApiView

urlpatterns = (
    path('register/', CreateUserApiView.as_view(), name='register-user'),
    path('login/', LoginApiView.as_view(), name='login-user'),
    # path('logout/')
)
