from django import template
from django.template.defaultfilters import safe
from datetime import datetime

register = template.Library()


# `simple_tag` expects to return an HTML string to visualize
@register.simple_tag
def list_of(values):
    items_string = [f'<li>{value}</li>' for value in values]

    return safe(f'<ul>{"".join(items_string)}</ul>')


@register.simple_tag
def current_time():
    now = datetime.now()

    return now.strftime("%H:%M:%S")

# `inclusion_tag`expects to return an HTML string based on a template
# example is in `user_tags.py`
# @register.inclusion_tag


# `tag` expects to return a template Node with `render` func
# @register.tag
