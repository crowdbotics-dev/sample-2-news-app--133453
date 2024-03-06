from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    UserProfileViewSet,
    UserProfileViewSet,
    UserProfileViewSet,
    UserProfileViewSet,
)

router = DefaultRouter()
router.register("userprofile", UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
