from django.shortcuts import render,redirect
from django.views import View
from store.models.orders import orders

class adminorder(View):
    def get(self,request):
        session = request.session.get('user')
        order = orders.objects.all()
        data = {
            'order' : order,

        }
        return render(request, 'admin_orders.html',data)
    def post(self,request):
        order = orders.objects.all()
        order_id = request.POST.get('order_id')
        if order_id:
            # order_data = orders.get_order_by_admin_id(order_id)
            order_data = orders.objects.get(ids=order_id)
            order_data.status=request.POST.get('order_status')
            order_data.save()






            return redirect('adminorder')
        return redirect('adminorder')