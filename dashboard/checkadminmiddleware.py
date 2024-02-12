from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

class CheckAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/web/') or request.path.startswith('/web'): 
            if not request.user.is_superuser:
                return redirect(reverse('h_login'))
            
        response = self.get_response(request)
        return response