from django.shortcuts import redirect

# ******* Authenticated *******
# auth prevent says those user is not auth which is not able to see dashboard
def auth(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapped_view

# ******* Guest *******
#gueat say those user register/login then it render dashboard then they not able to open register or login
def guest(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_function(request, *args, **kwargs)
    return wrapped_view