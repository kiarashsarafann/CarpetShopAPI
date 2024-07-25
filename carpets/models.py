from django.db import models


# Create your models here.

class Carpet(models.Model):
    title = models.CharField(max_length=128, verbose_name='نام فرش')
