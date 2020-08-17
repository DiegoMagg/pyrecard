from os import environ
from base64 import b64encode
from functools import wraps
from exceptions import MissingKey


def authorization(method):
    @wraps(method)
    def wrapper(self):
        headers = {'Authorization': None, 'Content-Type': 'application/json'}
        key = environ.get('WIRECARD_KEY')
        if key:
            headers['Authorization'] = 'Basic ' + str(b64encode(key.encode('utf-8')), "UTF-8")
            return method(self, headers)
        raise MissingKey('Wirecard key not found.')
    return wrapper
