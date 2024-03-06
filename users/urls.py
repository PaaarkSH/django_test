from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginView, UserView

urlpatterns = [
    path("sign-up/", UserView.as_view(), name="user-sign-up"),
    path("sign-in/", LoginView.as_view(), name="user-sign-in"),
    path("refresh/", TokenRefreshView.as_view(), name="user-token-refresh"),
]