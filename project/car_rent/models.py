from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Garage(models.Model):
    addres = models.CharField(max_length=400, verbose_name=_('Address'))

    class Meta:
        verbose_name = _('Garage')
        verbose_name_plural = _('Garages')

    def __str__(self):
        return self.addres


class Car(models.Model):
    name = models.CharField(max_length=400, verbose_name=_('Name'))
    reg_num = models.CharField(max_length=8, validators=[RegexValidator(regex=r'\d{4}\w{2}-\d',
                                                                        message='Невалидный номер (Пример: 1111АК-3')],
                               verbose_name=_('Reg. number'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('User'))
    garage = models.ForeignKey(Garage, on_delete=models.PROTECT, default=None, null=True, verbose_name=_('Garage'))

    def __str__(self):
        return self.name
