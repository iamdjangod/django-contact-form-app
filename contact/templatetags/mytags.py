from django import template

register = template.Library()


@register.simple_tag
def get_bootstrap_alert_msg_css_name(tags):
    return 'danger' if tags == 'error' else tags

