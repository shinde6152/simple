from django.shortcuts import render,redirect
from store.models.product import product
from store.models.category import category
from django.views import View


class index(View):
    def get(self,request):

        Products = product.get_all_products()
        categories = category.objects.all()
        cart= request.session.get('cart')
        if request.session.get('cart'):
            pass
        else:
            request.session['cart']={}

        categorys_id = request.GET.get("categorys")
        if categorys_id:
            Products = product.get_product_by_category_id(categorys_id)
        else:
            Products = product.get_all_products()

        data = {
            'categories': categories,
            'Products': Products
        }

        return render(request, 'index.html', data)

    def post(self,request):
        product = request.POST.get('product')
        cart=request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1

                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('/')












