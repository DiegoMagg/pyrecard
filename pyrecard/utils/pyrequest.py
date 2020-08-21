from requests import request
from os import environ
from pyrecard.utils.factory import header_factory, url_factory
from pyrecard.decorators import set_response_timeout


@set_response_timeout
def pyrequest(method, path, json={}):
    return request(
        method.upper(),
        url_factory(path),
        headers=header_factory(),
        json=json,
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )
