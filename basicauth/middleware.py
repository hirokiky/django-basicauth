from .basicauthutils import validate_request
from .compat import MiddlewareMixin
from .response import HttpResponseUnauthorized


class BasicAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not validate_request(request):
            return HttpResponseUnauthorized()
        return None
