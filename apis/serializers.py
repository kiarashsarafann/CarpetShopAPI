from rest_framework import serializers
from django.contrib.auth.models import User
from carpets.models import *


class CarpetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carpet
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
