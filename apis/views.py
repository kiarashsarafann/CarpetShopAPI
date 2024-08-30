from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers


class CarpetViewSet(viewsets.ModelViewSet):
    queryset = Carpet.objects.all()
    serializer_class = CarpetSerializers


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerilizers


class ReedViewSet(viewsets.ModelViewSet):
    queryset = Reed.objects.all()
    serializer_class = ReedSerilizers


class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializers


class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddToCartCarpetView(generics.CreateAPIView):
    serializer_class = AddCartItemCarpetSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        carpet = Carpet.objects.get(id=request.data['carpet'])
        item, created = CartItem.objects.get_or_create(cart=cart, carpet=carpet)
        item.quantity += int(request.data['quantity'])
        item.save()
        return Response(CartItemSerializer(item).data, status=status.HTTP_201_CREATED)


class AddToCartMaterialView(generics.CreateAPIView):
    serializer_class = AddCartItemMaterialSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        material = Material.objects.get(id=request.data['material'])
        item, created = CartItem.objects.get_or_create(cart=cart, material=material)
        item.quantity += int(request.data['quantity'])
        item.save()
        return Response(CartItemSerializer(item).data, status=status.HTTP_201_CREATED)


class RemoveCarpetFromCartView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart = Cart.objects.get(user=self.request.user)
        carpet = Carpet.objects.get(id=self.kwargs['carpet_id'])
        return CartItem.objects.get(cart=cart, carpet=carpet)

    def delete(self, request, *args, **kwargs):
        cart_item = self.get_object()
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RemoveMaterialFromCartView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart = Cart.objects.get(user=self.request.user)
        material = Material.objects.get(id=self.kwargs['material_id'])
        return CartItem.objects.get(cart=cart, material=material)

    def delete(self, request, *args, **kwargs):
        cart_item = self.get_object()
        cart_item.delete()
        return Response('حذف با موفقیت انجام شد')
