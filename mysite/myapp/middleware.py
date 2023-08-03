# middleware.py
from django.http import HttpResponse
from .models import AllowedIP
class IPValidationMiddleware:
    # ALLOWED_IPS = ['127.0.0.1', '192.168.0.1']  # Replace with your list of allowed IP addresses

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR', '')
        ALLOWED_IPS = [allowed_ip.ip_address for allowed_ip in AllowedIP.objects.all()]
        if client_ip not in ALLOWED_IPS:
            return HttpResponse('Access denied: Your IP address is not allowed.')
        response = self.get_response(request)
        return response