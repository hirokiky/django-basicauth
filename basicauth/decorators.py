from functools import wraps

from django.conf import settings

from basicauth.basicauthutils import extract_basicauth
from basicauth.response import HttpResponseUnauthorized


def basic_auth_required(func):
    @wraps(func)
    def _wrapped(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return HttpResponseUnauthorized()

        authorization_header = request.META['HTTP_AUTHORIZATION']
        ret = extract_basicauth(authorization_header)
        if not ret:
            return HttpResponseUnauthorized()

        username, password = ret

        if settings.BASICAUTH_USERS.get(username) != password:
            return HttpResponseUnauthorized()

        return func(request, *args, **kwargs)
    return _wrapped
