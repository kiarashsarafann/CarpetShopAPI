from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True, null=True, blank=True, verbose_name='شماره تماس')
    active_code = models.CharField(max_length=6, verbose_name='کد فعال سازی', default=00000)
    is_active = models.BooleanField(default=False)
    address = models.CharField(max_length=512, verbose_name='آدرس')

    class Meta:
        db_table = 'auth_user'
