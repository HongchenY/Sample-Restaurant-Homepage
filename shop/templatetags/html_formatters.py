from django import template

def currency_dollar(value):
    return f"{value:.2f} $"

register = template.Library()

register.filter("currency_dollar", currency_dollar)