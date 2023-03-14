from django.urls import path

from .views import UserLoginView, UserLogoutView, ProfileDetailView, ProfileUpdateView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
]