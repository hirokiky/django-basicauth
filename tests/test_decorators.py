from django.test import TestCase
from django.test.utils import override_settings


@override_settings(
    BASICAUTH_USERS={"username": "password"}
)
class TestBasicAuthDecorator(TestCase):

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

    def test__target_test__target(self):
        res = self.client.get("/decorated/target_test/", {'shouldauth': 1})
        self.assertEqual(res.status_code, 401)

    def test__target_test__ignored(self):
        res = self.client.get("/decorated/target_test/", {})
        self.assertEqual(res.content, b"Called; login=None")

    def test__target_test__it(self):
        res = self.client.get(
            "/decorated/target_test/", {'shouldauth': 1},
            HTTP_AUTHORIZATION="Basic dXNlcm5hbWU6cGFzc3dvcmQ="
        )
        self.assertEqual(res.content, b"Called; login=username")

    @override_settings(BASICAUTH_DISABLE=True)
    def test__disable_barriers(self):
        res = self.client.get(
            "/decorated/",
            HTTP_AUTHORIZATION="Basic aW52YWxpZDppbnZhbGlk"
        )
        self.assertEqual(res.content, b"Called; login=None")
