from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "name", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            user_id=validated_data["user_id"],
            name=validated_data["name"],
            password=validated_data["password"],  # 암호화 자동
        )
        return user
