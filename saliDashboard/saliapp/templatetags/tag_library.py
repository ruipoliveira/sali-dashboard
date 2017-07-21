from django import template

register = template.Library()


@register.filter()
def to_int_one_less(value):
    return long(value) - 1


@register.filter()
def to_int_one_more(value):
    return long(value) + 1
