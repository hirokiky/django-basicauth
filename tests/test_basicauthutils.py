from django.test import TestCase


class TestExtractBasicauth(TestCase):
    def _callFUT(self, *args, **kwargs):
        from basicauth.basicauthutils import extract_basicauth
        return extract_basicauth(*args, **kwargs)

    def test__it(self):
        actual = self._callFUT("Basic dXNlcm5hbWU6cGFzc3dvcmQ=")
        self.assertEqual(len(actual), 2)
        self.assertEqual(actual[0], 'username')
        self.assertEqual(actual[1], 'password')

    def test__cant_splitted_by_white_space__too_less(self):
        actual = self._callFUT("Basic")
        self.assertIsNone(actual)

    def test__cant_splitted_by_white_space__too_much(self):
        actual = self._callFUT("Basic auth string")
        self.assertIsNone(actual)

    def test__auth_string_wasnt_basic(self):
        actual = self._callFUT("Bearer dXNlcm5hbWU6cGFzc3dvcmQ=")
        self.assertIsNone(actual)

    def test__cant_decode_as_base64(self):
        actual = self._callFUT("invalid")
        self.assertIsNone(actual)

    def test__cant_decode_as_utf_8(self):
        actual = self._callFUT('pcaluaXI', encoding='utf-8')
        self.assertIsNone(actual)

    def test__auth_string_contains_too_much_delimiter(self):
        actual = self._callFUT('Basic dXNlcm5hbWU6cGFzc3dvcmQ6a2Fkb29t')
        self.assertIsNone(actual)
