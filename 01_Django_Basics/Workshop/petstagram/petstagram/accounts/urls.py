from django.urls import path, include

from petstagram.accounts.views import RegisterUserView, LoginUserView, ProfileDetailsView, EditProfileView, \
    DeleteProfileView, logout_user

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login-user'),
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('logout/', logout_user, name='logout-user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', EditProfileView.as_view(), name='profile-edit'),
        path('delete/', DeleteProfileView.as_view(), name='profile-delete'),
    ])),
)
