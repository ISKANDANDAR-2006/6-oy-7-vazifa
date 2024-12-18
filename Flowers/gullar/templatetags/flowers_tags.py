from django import template
from gullar.models import Type

register = template.Library()

@register.simple_tag
def get_types():
    return Type.objects.all()

