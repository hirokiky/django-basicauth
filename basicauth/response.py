from django.conf import settings
from django.http import HttpResponse


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

    def __init__(self):
        super(HttpResponseUnauthorized, self).__init__(
            """<html><head><title>Basic auth required</title></head>
               <body><h1>Authorization Required</h1></body></html>""",
        )
        realm = getattr(settings, 'BASICAUTH_REALM', 'Secure resource')
        self['WWW-Authenticate'] = 'Basic realm="{}"'.format(realm)
