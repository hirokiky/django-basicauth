import base64
import binascii

from django.conf import settings
from django.utils.crypto import constant_time_compare

from .compat import unquote_plus


def extract_basicauth(authorization_header, encoding='utf-8'):
    splitted = authorization_header.split(' ')
    if len(splitted) != 2:
        return None

    auth_type, auth_string = splitted

    if 'basic' != auth_type.lower():
        return None

    try:
        b64_decoded = base64.b64decode(auth_string)
    except (TypeError, binascii.Error):
        return None
    try:
        auth_string_decoded = b64_decoded.decode(encoding)
    except UnicodeDecodeError:
        return None

    splitted = auth_string_decoded.split(':')

    if len(splitted) != 2:
        return None

    username, password = map(unquote_plus, splitted)
    return username, password


def validate_request(request):
    """Check an incoming request.

    Returns:
        - True if authentication passed
        - Adding request['REMOTE_USER'] as authenticated username.
    """
    if getattr(settings, 'BASICAUTH_DISABLE', False):
        # Not to use this env
        return True

    if 'HTTP_AUTHORIZATION' not in request.META:
        return False

    authorization_header = request.META['HTTP_AUTHORIZATION']
    ret = extract_basicauth(authorization_header)
    if not ret:
        return False

    username, password = ret

    raw_pass = settings.BASICAUTH_USERS.get(username)
    if raw_pass is None:
        return False

    # To avoid timing atacks
    # https://security.stackexchange.com/questions/83660/simple-string-comparisons-not-secure-against-timing-attacks
    if not constant_time_compare(raw_pass, password):
        return False

    request.META['REMOTE_USER'] = username
    return True
