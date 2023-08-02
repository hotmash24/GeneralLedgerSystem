
from django.shortcuts import redirect
from django.contrib.auth import logout
from myapp.apps import locationUnit
from django.conf import settings
def ul_code_context(request):
    ul_code_login = request.session.get('UL_CODE', None)
    ul_code = ''
    count = 0
    location = locationUnit
    
    if ul_code_login is not None:
        for ul in location:
            if ul['ul_code'] == int(ul_code_login):
                ul_code = f"{ul['ul_code']}-{ul['unit_description']}"
                break
    return {'ul_code': ul_code}

class SessionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'user_authenticated' in request.session and request.session['user_authenticated'] == True:
            # User is authenticated, proceed with the request
            return self.get_response(request)
        else:
            # User is not authenticated, redirect to the login page
            return redirect('login')
