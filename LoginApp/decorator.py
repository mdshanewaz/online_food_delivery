from django.http import HttpResponse
from django.shortcuts import redirect
from LoginApp.models import ProfileModel, User

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('LoginApp:profile')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func