from django import template

register = template.Library()

"""
Custom filters should be registered to be used in templates.
Primarily used with only one parameter.
"""


def only_with_condition(numbers, condition_func):
    return [x for x in numbers if condition_func(x)]


@register.filter
def only_odd(numbers):
    """ My custom filter function """
    return only_with_condition(numbers, lambda x: x % 2 == 1)


@register.filter
def only_even(numbers):
    """ My custom filter function """
    return only_with_condition(numbers, lambda x: x % 2 == 0)


@register.filter
def only_positive(numbers):
    """ My custom filter function """
    return only_with_condition(numbers, lambda x: x > 0)


@register.filter
def only_negative(numbers):
    """ My custom filter function """
    return only_with_condition(numbers, lambda x: x < 0)
