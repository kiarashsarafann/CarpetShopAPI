from django.db import models


class Carpet(models.Model):
    title = models.CharField(max_length=64, verbose_name='نام فرش')
    image = models.ImageField(upload_to='carpets', verbose_name="عکس")
    size = models.ForeignKey(to='Size', on_delete=models.CASCADE, related_name='سایز', verbose_name="سایز فرش")
    material = models.ForeignKey(to='Material', on_delete=models.CASCADE, related_name='جنس', verbose_name='جنس فرش')
    reed = models.ForeignKey(to='Reed', on_delete=models.CASCADE, related_name='شانه', verbose_name='شانه قرش')
    design = models.ForeignKey(to='Design', on_delete=models.CASCADE, related_name='نقشه', verbose_name='نقشه فرش')
    price = models.IntegerField(verbose_name='قیمت', default=0)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=16, verbose_name="سایز")

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=64, verbose_name='جنس')
    image = models.ImageField(upload_to='materials', verbose_name="عکس")
    price = models.IntegerField(verbose_name='قیمت')

    def __str__(self):
        return self.title


class Reed(models.Model):
    title = models.CharField(max_length=64, verbose_name='شانه')

    def __str__(self):
        return self.title


class Design(models.Model):
    title = models.CharField(max_length=64, verbose_name="نقشه")
    image = models.ImageField(upload_to='design', verbose_name='عکس')

    def __str__(self):
        return self.title
