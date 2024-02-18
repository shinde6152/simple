from django.shortcuts import render,redirect


def simple_middleware(get_response):

    def middleware(request):
        if not request.session.get('id'):
            return redirect("login")

        response = get_response(request)
        return response

    return middleware