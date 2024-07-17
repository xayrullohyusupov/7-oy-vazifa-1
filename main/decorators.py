from django.http import HttpResponseForbidden
from functools import wraps

def isOwner(model):
    def decorator(view_func):
        @wraps(view_func)
        def wrap(request,id, *args, **kwargs):
            obj = model.Blog.objects.get(id=id)
            if request.user == obj.author:
                return view_func(request,id, *args, **kwargs)
            else:
                return HttpResponseForbidden('index')
        return wrap
    return decorator
