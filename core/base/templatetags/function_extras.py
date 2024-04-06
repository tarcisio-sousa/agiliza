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


@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    if not value:
        return ''
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url


@register.simple_tag(takes_context=True)
def url_set_param(context, **kwargs):
    filtered_querystring = ['{}={}'.format(k, v) for k, v in kwargs.items() if v]
    encoded_querystring = '&'.join(filtered_querystring)
    url = '{}?{}'.format(context.request.path, encoded_querystring)
    return url


@register.filter(name='get_color_status')
def get_color_status(color):
    if (color > 0):
        return 'red'
    if (color == 0):
        return 'yellow'
    return 'blue'
