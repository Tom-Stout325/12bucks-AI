from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, {})

@register.filter
def add_class(value, arg):
    """Add a CSS class to a form field widget."""
    return value.as_widget(attrs={'class': arg})