from functools import wraps

from django.shortcuts import redirect


def authentication_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:

            return view_func(request, *args, **kwargs)
        else:
            return redirect('error page')
    return wrapper




