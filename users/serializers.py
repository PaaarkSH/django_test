from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def is_valid(self, raise_exception=True):
        data = super().is_valid(raise_exception=True)
        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            raise serializers.ValidationError("Invalid username or password.")
        self.user = user
        return data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        return user

    def is_valid(self, raise_exception=True):
        data = super().is_valid(raise_exception=True)
        user = User.objects.create_user(username=data["username"], password=data["password"])
        self.user = user
        return data
