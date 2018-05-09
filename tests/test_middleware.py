import django
from django.test import TestCase
from django.test.utils import override_settings

if django.VERSION >= (1, 10):
    middleware_settings = 'MIDDLEWARE'
else:
    middleware_settings = 'MIDDLEWARE_CLASSES'


@override_settings(
    BASICAUTH_USERS={"username": "password"},
    **{middleware_settings: ['basicauth.middleware.BasicAuthMiddleware']}
)
class TestBasicAuthMiddleware(TestCase):
    def test__it(self):
        res = self.client.get(
            "/decorated/",
            HTTP_AUTHORIZATION="Basic dXNlcm5hbWU6cGFzc3dvcmQ="
        )
        self.assertEqual(res.content, b"Called; login=username")

    def test__hasnt_authorization_header(self):
        res = self.client.get("/decorated/")
        self.assertEqual(res.status_code, 401)

    def test__invalid_user(self):
        res = self.client.get(
            "/decorated/",
            HTTP_AUTHORIZATION="Basic aW52YWxpZDppbnZhbGlk"
        )
        self.assertEqual(res.status_code, 401)

    @override_settings(BASICAUTH_DISABLE=True)
    def test__disable_barriers(self):
        res = self.client.get(
            "/decorated/",
            HTTP_AUTHORIZATION="Basic aW52YWxpZDppbnZhbGlk"
        )
        self.assertEqual(res.content, b"Called; login=None")
