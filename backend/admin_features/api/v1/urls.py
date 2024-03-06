from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ContentModerationViewSet,
    UserManagementViewSet,
    ContentModerationViewSet,
    UserManagementViewSet,
    ContentModerationViewSet,
    UserManagementViewSet,
    ContentModerationViewSet,
    UserManagementViewSet,
)

router = DefaultRouter()
router.register("contentmoderation", ContentModerationViewSet)
router.register("usermanagement", UserManagementViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
