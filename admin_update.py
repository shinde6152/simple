from django.shortcuts import render,redirect
from django.views import View
from store.models.product import product
from django.utils.decorators import method_decorator
from store.middlewares.admin_auth import simple_middleware

class adminupdate(View):
    @method_decorator(simple_middleware)
    def get(self,request):
        update_ids = request.GET.get('update_ids')
        request.session['update_ids'] = update_ids
        if update_ids:
            product_data = product.get_product_by_admin_update(update_ids)

        data = {
            'product_data'  : product_data
        }




        return render(request,'admin_update.html',data)
    @method_decorator(simple_middleware)
    def post(self,request):
        try:
            product_id = request.session.get('update_ids')
            product_data = product.objects.get(id=product_id)

            product_data.PRODUCT = request.POST.get('product')
            product_data.DESCRIPTION = request.POST.get('description')
            product_data.PRICE = request.POST.get('price')
            product_data.IMAGE = request.FILES['image']

            product_data.save()
        except:
            pass


        return redirect('admin_view')

