import io
import sys

PY3 = sys.version_info[0] == 3

if PY3:  # pragma: no cover
    from urllib.parse import urlparse

    binary_types = bytes
    string_types = (str,)
    StringIO = io.StringIO
else:  # pragma: no cover
    from urlparse import urlparse  # noqa

    binary_types = str
    string_types = (basestring,)  # noqa
    StringIO = io.BytesIO
