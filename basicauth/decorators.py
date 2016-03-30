from functools import wraps

from .response import HttpResponseUnauthorized
from .basicauthutils import validate_request


def basic_auth_required(func):
    @wraps(func)
    def _wrapped(request, *args, **kwargs):
        validated_username = validate_request(request)
        if validated_username is None:
            return HttpResponseUnauthorized()
        else:
            request.META['REMOTE_USER'] = validated_username
            return func(request, *args, **kwargs)
    return _wrapped
