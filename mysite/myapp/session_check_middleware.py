# # session_check_middleware.py

# from django.shortcuts import redirect
# # from myapp.apps import count

# class SessionCheckMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):

#         if 'login_count' not in request.session:
#             if 'user_authenticated' not in request.session or not request.session['user_authenticated']:
#                     # If the user is not authenticated, you can redirect them to the login page
#                 return redirect('login')
#         else:
#             ip = request.session['login_count']
#             if ip > 0:
#                 if 'user_authenticated' not in request.session or not request.session['user_authenticated']:
#                     return redirect('login')
#         response = self.get_response(request)
#         return response
