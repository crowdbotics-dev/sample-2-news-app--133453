from rest_framework import serializers
from admin_features.models import (
    ContentModeration,
    UserManagement,
    ContentModeration,
    UserManagement,
)


class ContentModerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentModeration
        fields = "__all__"


class UserManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManagement
        fields = "__all__"
