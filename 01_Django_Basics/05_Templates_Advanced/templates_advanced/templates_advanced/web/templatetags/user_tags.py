from django import template

register = template.Library()


@register.inclusion_tag('tags/profile_avatar.html', takes_context=True)
def get_profile_avatar(context):
    # Returns `context`, much like in views

    user = context.request.user

    user_fullname = f'{user.first_name} {user.last_name}' if user.is_authenticated else 'AnonymousUser'

    return {
        'user_fullname': user_fullname,
    }


@register.inclusion_tag('tags/initials.html', takes_context=True)
def get_user_initials(context):

    user = context.request.user

    initials = user.first_name[0] + user.last_name[0] if user.is_authenticated else 'AU'

    return {
        'initials': initials,
    }
