from django.forms import ModelForm
from . import models


class CarForm(ModelForm):
    class Meta:
        model = models.Car
        fields = ['name', 'reg_num', 'user']
