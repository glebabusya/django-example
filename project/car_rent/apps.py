from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CarRentConfig(AppConfig):
    name = 'car_rent'
    verbose_name = _('Car rent')
