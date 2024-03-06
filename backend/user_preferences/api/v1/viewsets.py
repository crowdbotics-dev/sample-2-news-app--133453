from rest_framework import authentication
from user_preferences.models import UserProfile, UserProfile, UserProfile
from .serializers import (
    UserProfileSerializer,
    UserProfileSerializer,
    UserProfileSerializer,
)
from rest_framework import viewsets


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UserProfile.objects.all()
