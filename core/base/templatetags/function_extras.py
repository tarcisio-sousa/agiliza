from django import template
from num2words import num2words

register = template.Library()


@register.filter(name='in_full_format')
def in_full_format(value):
    if value.find(','):
        value = value.split(',')
        number_integer = int(value[0].replace('.', ''))
        number_decimal = int(value[1])
    else:
        number_integer = int(value.replace('.', ''))
        number_decimal = 0

    currency_integer = ' real' if number_integer == 1 else ' reais'

    currency_decimal = ' centavo' if number_decimal == 1 else ' centavos'

    text_integer = (num2words(number_integer, lang='pt_BR') + str(currency_integer)) if number_integer > 0 else ''

    text_decimal = (num2words(number_decimal, lang='pt_BR') + str(currency_decimal)) if number_decimal > 0 else ''

    if number_integer > 0 and number_decimal > 0:
        result = text_integer + ' e ' + text_decimal
    else:
        result = text_integer + text_decimal

    return result.capitalize()
