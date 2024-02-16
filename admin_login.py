from django.shortcuts import render,redirect
from django.views import View
from store.models.admin_login import admin_login

class admin_log(View):
    def get(self,request):


        return render(request,'admin_login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            login_data=admin_login.objects.get(email=email)
            if login_data:
                if login_data.password == password:
                    request.session['user']=login_data.email
                    request.session['password']=login_data.password
                    return redirect('admin_view')
        except:
            pass
        return render(request,'admin_login.html')