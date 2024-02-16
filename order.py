from django.shortcuts import render,redirect
from django.views import View
from store.models.product import product
from store.models.orders import orders
from store.middlewares.auth import simple_middleware
from django.utils.decorators import method_decorator


class order_display(View):

    @method_decorator(simple_middleware)
    def get(self,request):
        user = request.session.get('id')
        order= orders.get_order_by_id(user)
        if 'cart' in request.session:
            del request.session['cart']
        else:
            print("item not removed from session")

        return render(request,"order.html",{'order':order})