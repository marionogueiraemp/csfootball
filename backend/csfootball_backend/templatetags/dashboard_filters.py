from django import template
from django.template.defaultfilters import floatformat
from ..utils import DashboardUtils

register = template.Library()


@register.filter
def format_timestamp(value):
    return DashboardUtils.format_timestamp(value)


@register.filter
def alert_class(value):
    return DashboardUtils.get_alert_class(value)


@register.filter
def format_memory(value):
    return DashboardUtils.format_memory_usage(value)


@register.filter
def percentage(value):
    return floatformat(value * 100, 2) + '%'
