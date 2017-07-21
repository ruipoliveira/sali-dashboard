from django import template

register = template.Library()


@register.filter()
def to_int_one_less(value):
    return float(value) + 1


@register.filter()
def to_int_one_more(value):
    return float(value) - 1
