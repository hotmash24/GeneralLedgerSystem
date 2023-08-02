
from django import template
from num2words import num2words

register = template.Library()

def amount_to_words_with_cents(amount):
    whole_part, decimal_part = str(amount).split('.')
    whole_part = int(whole_part)
    decimal_part = int(decimal_part) if decimal_part else 0

    words_whole = num2words(whole_part)
    words_decimal = num2words(decimal_part).replace('-', ' ').capitalize() + " cents" if decimal_part > 0 else ""

    result = words_whole + (" and " + words_decimal if words_decimal else "")
    return result

register.filter('amount_to_words_with_cents', amount_to_words_with_cents)