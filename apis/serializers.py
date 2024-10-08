import secrets
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from carpets.models import Carpet, Reed, Size, Design, Material
from users.models import CustomUser
from cart.models import Cart, CartItem


class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class MaterialSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ReedSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Reed
        fields = '__all__'


class DesignSerializers(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'


class CarpetSerializers(serializers.ModelSerializer):
    material = serializers.StringRelatedField(read_only=True)
    reed = serializers.StringRelatedField(read_only=True)
    size = serializers.StringRelatedField(read_only=True)
    design = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Carpet
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    carpet = CarpetSerializers()
    material = MaterialSerilizers()

    class Meta:
        model = CartItem
        fields = ['id', 'carpet', 'material', 'quantity', 'get_total_price']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = CartItem
        fields = ['id', 'items']


class AddCartItemCarpetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['carpet', 'quantity']


class AddCartItemMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['material', 'quantity']


class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    first_name = serializers.CharField(
        required=True
    )
    last_name = serializers.CharField(
        required=True
    )
    address = serializers.CharField(
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'password', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
        )
        user.is_active = True
        user.save()
        return user
