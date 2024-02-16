from django.shortcuts import render,redirect
from django.views import View
from store.models.product import product
from store.models.orders import orders
from store.models.sign import sign


class cartpage(View):
    def get(self, request):
        cart = request.session.get('cart')
        cart_keys =list(cart.keys())
        cart_values=list(cart.values())
        # Now filter the product using cart
        products = product.get_products_by_cart(cart)

        data = {
            'products': products,
            'cart_values': cart_values,
        }
        return render(request,'cartpage.html',data)

    def post(self, request):
        phone = request.POST.get('phone')
        address = request.POST.get('Address')
        cart = request.session.get('cart')
        customer = request.session.get('id')
        products_obj = product.get_product_by_id(list(cart.keys()))
        print(phone,address,cart,customer,products_obj)
        for products in products_obj:
            order = orders(customer=sign(id=customer),product=products,price=products.PRICE,quantity=cart.get(str(products.id)),phone=phone,address=address)
            order.save()
        cart.clear()
        return redirect('order')
    
