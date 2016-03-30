from django.conf.urls import url
from django.http import HttpResponse

from basicauth.decorators import basic_auth_required


def naked_view(request, *args, **kwargs):
    username = request.META.get('REMOTE_USER')
    return HttpResponse("Called; login=%s" % username)


decorated_view = basic_auth_required(naked_view)


urlpatterns = [
    url(r'^decorated/', decorated_view),
    url(r'^naked/', naked_view),
]
