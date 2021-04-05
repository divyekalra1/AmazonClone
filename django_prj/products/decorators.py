from django.http import HttpResponse

def authorized(allowed_users=[]):
    def decorator(view_func):
        def wrapper(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_users:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("<h1>You are not authorized to view this page</h1>")
        return wrapper
    return decorator
