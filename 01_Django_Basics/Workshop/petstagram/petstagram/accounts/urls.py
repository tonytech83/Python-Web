from django.urls import path, include

from petstagram.accounts.views import RegisterView, LoginView, ShowProfileDetailsView, EditProfileView, \
    DeleteProfileView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>/', include([
        path('', ShowProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', EditProfileView.as_view(), name='profile-edit'),
        path('delete/', DeleteProfileView.as_view(), name='profile-delete'),
    ])),
)
