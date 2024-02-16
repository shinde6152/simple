from django.shortcuts import redirect
from django.views import View

class adminlogout(View):
    def get(self,request):
        request.session.clear()
        return redirect('/')