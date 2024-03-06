from rest_framework import authentication
from admin_features.models import (
    ContentModeration,
    UserManagement,
    ContentModeration,
    UserManagement,
    ContentModeration,
    UserManagement,
)
from .serializers import (
    ContentModerationSerializer,
    UserManagementSerializer,
    ContentModerationSerializer,
    UserManagementSerializer,
    ContentModerationSerializer,
    UserManagementSerializer,
)
from rest_framework import viewsets


class ContentModerationViewSet(viewsets.ModelViewSet):
    serializer_class = ContentModerationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ContentModeration.objects.all()


class UserManagementViewSet(viewsets.ModelViewSet):
    serializer_class = UserManagementSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UserManagement.objects.all()
