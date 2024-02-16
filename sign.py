from django.shortcuts import render,redirect
from store.models.product import product
from store.models.category import category
from django.views import View
from store.models.sign import sign


class signup(View):
    def get(self,request):
        return render(request,'sign.html')


    def post(self,request):
        try:
            if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                print(name, email, password)

                sign_obj = sign(name=name, email=email, password=password)
                sign_obj.save()
        except:
            pass


        return redirect("login")
