from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "objects",
            "email",
            "is_active",
            "created_at",
            "USERNAME_FIELD"
        )
