from functools import wraps

from .response import HttpResponseUnauthorized
from .basicauthutils import validate_request


def basic_auth_required(func):
    @wraps(func)
    def _wrapped(request, *args, **kwargs):
        if not validate_request(request):
            return HttpResponseUnauthorized()
        return func(request, *args, **kwargs)
    return _wrapped
