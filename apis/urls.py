from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from users.views import *
from .views import *

router = routers.DefaultRouter()
router.register('carpet', CarpetViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', obtain_auth_token, name='token_generator'),
    path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]
