from django import template
#from myapp.views import has_perm1_or_perm2
from internship.roles import allowed_users

register = template.Library()

@register.filter
def user_has_perms(user):
    return allowed_users(user)
