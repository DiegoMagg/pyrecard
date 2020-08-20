from functools import wraps
from requests.exceptions import ConnectTimeout
from pyrecard.utils.factory import response_factory, url_factory


def set_response_timeout(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ConnectTimeout:
            return response_factory(408, {'error': f'Connection to {url_factory()} timed out'})
    return wrapper
