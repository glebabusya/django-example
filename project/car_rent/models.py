from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Garage(models.Model):
    addres = models.CharField(max_length=400)

    def __str__(self):
        return self.addres


class Car(models.Model):
    name = models.CharField(max_length=400)
    reg_num = models.CharField(max_length=8, validators=[RegexValidator(regex=r'\d{4}\w{2}-\d',
                                                                        message='Невалидный номер (Пример: 1111АК-3')])
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    garage = models.ForeignKey(Garage, on_delete=models.PROTECT, default=None, null=True)

    def __str__(self):
        return self.name
