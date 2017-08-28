from .basicauthutils import validate_request
from .response import HttpResponseUnauthorized


class BasicAuthMiddleware:
    def process_request(self, request):
        if not validate_request(request):
            return HttpResponseUnauthorized()
        return None
