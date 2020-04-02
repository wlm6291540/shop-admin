from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    joined_time = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()

    def get_last_login(self, obj):
        return obj.last_login.strftime('%Y-%m-%d %H:%M:%S') if obj.last_login else None

    def get_joined_time(self, obj):
        return obj.date_joined.strftime('%Y-%m-%d %H:%M:%S') if obj.date_joined else None

    def get_status(self, obj):
        return '启用' if obj.is_active else '禁用'

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'status', 'last_login', 'joined_time', 'desc']


class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_active']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'phone', 'is_active', 'desc']


class UserPasswordUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password']


class UserActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_active']
