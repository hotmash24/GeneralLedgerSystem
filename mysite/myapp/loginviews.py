from django.shortcuts import render, redirect

from django.shortcuts import redirect
from django.contrib.auth import logout
from myapp.apps import locationUnit
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse

def login_view(request):

    location = locationUnit
    if request.method == 'POST':
        username = request.POST['username'].upper()
        password = request.POST['password'].upper()
        ul_code_login = request.POST['location']
        request.session['UL_CODE'] = ul_code_login
        print('ul_code_login:',ul_code_login)
        request.session['user_authenticated'] = True
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
                
            # return HttpResponseRedirect('/disbursement/')
            return redirect('home')
        else:
           return render(request, 'login.html', {'error': 'Invalid username or password.', 'location': location})

    # print('Unit Location:',location)
    return render(request, 'login.html',  {'location': location})


def logout_view(request):
    request.session.flush()
    # request.session['login_count']=0
    return JsonResponse({'message': 'Logout successful'})
    # return HttpResponseRedirect('/login/')

# def logout_view(request):
#     request.session.flush()
#     return JsonResponse('login')
    # return JsonResponse(list(application_list), safe=False) 

    

def get_client_ip(request):
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR', '')
    ip_address = client_ip
    print('IP Address:',client_ip)
    return HttpResponse(f"Your IP address is: {ip_address}")