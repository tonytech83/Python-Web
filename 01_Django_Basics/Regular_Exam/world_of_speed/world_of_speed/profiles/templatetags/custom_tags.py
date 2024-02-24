from django import template

register = template.Library()


@register.filter
def sum_prices(car_set):
    return sum(car.price for car in car_set)
