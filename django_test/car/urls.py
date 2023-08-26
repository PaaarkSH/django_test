from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"image", views.CarImageViewSet, basename="image")
router.register(r"", views.CarViewSet, basename="car")

urlpatterns = [
    path("", include(router.urls)),
]
