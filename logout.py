from django.shortcuts import render,redirect
from django.views import View


class logout(View):
    def get(self,request):
        request.session.clear()

        return redirect('/')