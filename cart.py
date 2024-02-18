from django import template

register = template.Library()

@register.filter (name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter (name='cart_quantity')
def cart_quantity(products,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==products.id:
            return cart.get(id)
    return 0;

@register.filter (name='cart_length')
def cart_length(cart):
    keys = cart.keys()
    for ii in keys:
        return print('length of cart',ii)

@register.filter (name='price_total')
def price_total(products,cart):
    return products.PRICE*cart_quantity(products,cart)

@register.filter(name="final_price")
def final_price(products,cart):
    sum = 0
    for product in products:
        sum += price_total(product, cart)
    return sum

@register.filter(name="multiply")
def currency(number , number1):
    return number * number1