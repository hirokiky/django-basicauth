from .basicauthutils import validate_request
from .response import HttpResponseUnauthorized


class BasicAuthMiddleware:
    def process_request(self, request):
        validated_username = validate_request(request)
        if validated_username is None:
            return HttpResponseUnauthorized()
        else:
            request.META['REMOTE_USER'] = validated_username
            return None
