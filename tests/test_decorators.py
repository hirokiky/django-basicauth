from django.test import TestCase
from django.test import RequestFactory
from django.test.utils import override_settings


@override_settings(
    BASICAUTH_USERS={"username": "password"}
)
class TestBasicAuthDecorator(TestCase):
    rf = RequestFactory()

    def _callFUT(self, *args, **kwargs):
        from basicauth.decorators import basic_auth_required

        def dummy_view(*args, **kwargs):
            return "Called"

        return basic_auth_required(dummy_view)(*args, **kwargs)

    def test__it(self):
        req = self.rf.get("/", HTTP_AUTHORIZATION="Basic dXNlcm5hbWU6cGFzc3dvcmQ=")
        res = self._callFUT(req)
        self.assertEqual(res, "Called")

    def test__hasnt_authorization_header(self):
        req = self.rf.get("/")
        res = self._callFUT(req)
        self.assertEqual(res.status_code, 401)

    def test__invalid_user(self):
        req = self.rf.get("/", HTTP_AUTHORIZATION="Basic aW52YWxpZDppbnZhbGlk")
        res = self._callFUT(req)
        self.assertEqual(res.status_code, 401)
