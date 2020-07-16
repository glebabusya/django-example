from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from django.utils.translation import gettext_lazy as _
from . import models


class CarInline(StackedInline):
    model = models.Car
    fk_name = 'garage'
    extra = 1


def sell_car(modeladmin, request, queryset):
    queryset.update(garage=None)


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    actions = [sell_car]
    list_display = ['name', 'garage']


@admin.register(models.Garage)
class GarageAdmin(admin.ModelAdmin):
    actions = ['addres_reset']
    inlines = [CarInline]

    def addres_reset(self, request, queryset):
        queryset.update(addres='')

    addres_reset.short_description = _('reset garage addres')
