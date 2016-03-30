from django.conf.urls import url
from django.http import HttpResponse

from basicauth.decorators import basic_auth_required


def naked_view(request, *args, **kwargs):
    return HttpResponse("Called")


decorated_view = basic_auth_required(naked_view)


urlpatterns = [
    url(r'^decorated/', decorated_view),
    url(r'^naked/', naked_view),
]
