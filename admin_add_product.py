from django.shortcuts import render,redirect
from django.views import View
from store.models.product import product
from store.models.category import category
from django.utils.decorators import method_decorator
from store.middlewares.admin_auth import simple_middleware

class admin_addproduct(View):

    def get(self,request):

        return render(request,'add_product.html')


    @method_decorator(simple_middleware)
    def post(self,request):
        if request.method == 'POST':

            products=request.POST.get('product')
            category=request.POST.get('category')
            description=request.POST.get('description')
            price=request.POST.get('price')
            print(product,description,price)

            product_obj = product.objects.all()
            product_obj = product(PRODUCT=products,DESCRIPTION=description,PRICE=price)
            if len(request.FILES) != 0:
                product_obj.IMAGE = request.FILES['image']
            product_obj.save()

            return redirect('admin_view')
        return render(request,'add_product.html')