import random
from django.contrib.auth import login, logout, authenticate
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from apis.serializers import UserSerializers, CarpetSerializers
from .models import CustomUser


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        user: CustomUser = CustomUser.objects.filter(email__iexact=email).first()
        if user is not None:
            entered_password = request.data.get('password')
            user_password = user.check_password(entered_password)
            if user_password:
                token = Token.objects.get_or_create(user=user)[0].key
                login(request, user)
                user.is_active = True
                user.save()
                return Response({
                    'id': user.id, 'email': user.email, 'username': user.username, 'token': token,
                    'message': 'ورود با موفقیت انجام شد'

                })
            else:
                return Response('رمز ورود اشتباه است')
        else:
            return Response('نام کاربری وجود ندارد')
