from django import template

register = template.Library()

@register.filter
def currency(value):
    try:
        value = float(value)  # Ensure the value is a float
        return "Rp {:,.0f}".format(value).replace(',', '.')  # Format with thousands separator
    except (ValueError, TypeError):
        return value  # Return original value if error occurs
