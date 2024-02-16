from django.shortcuts import render,redirect
from store.models.product import product
from store.models.category import category
from django.views import View
from store.models.sign import sign


class login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            Email = request.POST.get('email')
            Password = request.POST.get('password')
            print(Email, Password)

            user = sign.objects.get(email=Email)

            if user.password == Password:
                request.session['user'] = user.name
                request.session['id'] = user.id
                return redirect('/')

        return render(request, 'login.html')
