from django.utils.safestring import SafeString

from .. import models
from django.template import Library
from django.template.defaultfilters import stringfilter
from django.core.exceptions import FieldError

register = Library()


@stringfilter
@register.filter()
def cut(line, numb):
    if len(line) > numb:
        return line[:numb] + '...'
    return line


@register.simple_tag
def cars_in_garage(garage_id=None, order=''):
    res = ''
    try:
        cars = models.Car.objects.filter(garage_id=garage_id).order_by(order)
    except FieldError:
        cars = models.Car.objects.filter(garage_id=garage_id)
        print('qweqwe')
    for car in cars:
        res += f'{car} '
    return res


@register.simple_tag
def abc():
    a = "<a href='google.com'>abcasd</a>"
    return SafeString(a)
