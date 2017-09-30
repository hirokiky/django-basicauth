import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    from urllib import unquote_plus  # NOQA
else:
    from urllib.parse import unquote_plus  # NOQA
