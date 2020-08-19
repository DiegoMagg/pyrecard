from os import environ
from re import match
from base64 import b64encode
from exceptions import MissingKey, InvalidKey


def get_b64(key=None):
    if not key:
        raise MissingKey('Wirecard key not found.')
    if not match(r'\w{32}:\w{40}', key):
        raise InvalidKey('Invalid key')
    return {'Authorization': f'Basic {str(b64encode(key.encode("UTF-8")), "UTF-8")}'}


def get_header():
    headers = {'User-Agent': 'Pyrecard', 'Content-Type': 'application/json'}
    if environ.get('PYRECARD_ENV') == 'production':
        return {**headers, **get_b64(environ.get('PRODUCTION_KEY'))}
    return {**headers, **get_b64(environ.get('SANDBOX_KEY'))}
