from rest_framework import serializers
from authentication.models import User, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]
