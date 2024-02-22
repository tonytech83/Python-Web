from django import template

register = template.Library()


@register.filter
def range_of_stars(value):
    return range(value)
