from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import delete_all_users, login, logout_view, profile, register


urlpatterns = [
	path("register/", register, name="register"),
	path("login/", login, name="login"),
	path("logout/", logout_view, name="logout"),
	path("profile/", profile, name="profile"),
	path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
	path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
  
	path("delete_all_users/", delete_all_users, name="delete_all_users"), # For testing purposes only
]
