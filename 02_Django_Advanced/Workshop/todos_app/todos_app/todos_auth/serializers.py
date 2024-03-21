from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    # Overwrites `create()` to hash the password with `create_user()` of `UserModel` manager
    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    # to prevent hashed password to be returned in response
    def to_representation(self, *args, **kwargs):
        representation = super().to_representation(*args, **kwargs)
        representation.pop('password', None)

        return representation
