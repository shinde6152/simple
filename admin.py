from django.shortcuts import render,redirect
from django.views import View
from store.models.product import product
from store.models.category import category
from django.utils.decorators import method_decorator
from store.middlewares.admin_auth import simple_middleware

class admin_view(View):

    @method_decorator(simple_middleware)
    def get(self,request):
        products = product.objects.all()
        product_ids = request.GET.get('product_id')
        if product_ids:
            product_obj = product.get_product_by_admin_id(product_ids)
            product_obj.delete()
        data = {
            'products': products,
        }
        return render(request,'admin_dashbord.html',data)

    def post(self,request):
        return render(request,'admin_dashbord.html')