from django.shortcuts import redirect
from django.urls import reverse
from Landing.urls import urlpatterns

class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path matches a URL in your app
        if request.path.startswith('/POS/'):
            if not request.user.is_authenticated:
                return redirect('/')
            
        if request.path=='/' or request.path=='/logIn' or request.path=='/signIn':
            if request.user.is_authenticated:
                return redirect('/POS/')
        # Otherwise, continue to the original request
        response = self.get_response(request)
        return response