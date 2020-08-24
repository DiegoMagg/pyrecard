from requests import request
from requests.exceptions import ConnectTimeout, ReadTimeout
from os import environ
from pyrecard.utils.factory import header_factory, url_factory, response_factory


def pyrequest(method, path, json={}):
    try:
        return request(
            method.upper(),
            url_factory(path),
            headers=header_factory(),
            json=json,
            timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
        )
    except (ConnectTimeout, ReadTimeout):
        return response_factory(408, {'error': f'Connection to {url_factory()} timed out'})
