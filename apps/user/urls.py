from django.urls import path

from apps.user.views import UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView

app_name = 'user'

urlpatterns = [
    # user
    path('users/', UserListAPIView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
]