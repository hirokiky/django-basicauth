from .basicauthutils import validate_request
from .response import HttpResponseUnauthorized
from django.utils.deprecation import MiddlewareMixin


class BasicAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not validate_request(request):
            return HttpResponseUnauthorized()
        return None
