from functools import wraps

from .response import HttpResponseUnauthorized
from .basicauthutils import validate_request


def basic_auth_required(func=None,
                        target_test=(lambda request: True)):
    def actual_decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if target_test(request) and not validate_request(request):
                return HttpResponseUnauthorized()
            return view_func(request, *args, **kwargs)
        return _wrapped

    if func:
        return actual_decorator(func)
    else:
        return actual_decorator
