from rest_framework import serializers
from user_preferences.models import UserProfile, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
