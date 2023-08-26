from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r"signup", views.UserViewSet, basename="user")  # 회원가입 crud

urlpatterns = [
    path(
        "login/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # jwt 를 통한 login  # post user_id, password
    path(
        "refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # jwt 를 통한 토큰 갱신  # post refresh_token
    path("logout/", views.logout),  # 로그아웃은 simplejwt 에 구현되어있지 않아서 직접 구현
    path("", include(router.urls)),
]
