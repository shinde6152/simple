from django.shortcuts import redirect

def simple_middleware(get_response):

    def middleware(request):
        print(request.session.get('user'))
        if not request.session.get('user'):
            print("admin needs to be logged in")
            return redirect('admin_log')

        response = get_response(request)
        return response
    return middleware