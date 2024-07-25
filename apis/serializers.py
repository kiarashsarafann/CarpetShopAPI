import secrets
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

from carpets.models import *
from users.models import *


class CarpetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carpet
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user
