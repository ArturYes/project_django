from django import template

register = template.Library()


@register.filter
def media_url(data):
    if data:
        return f"/media/{data}"
    return "#"


@register.filter
def check_group(user):
    return user.groups.filter(name='Moderator').exists()
