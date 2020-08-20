from os import environ
from re import match
from base64 import b64encode
from pyrecard.exceptions import MissingKey, InvalidKey
from pyrecard.sdk import VERSION


def get_b64(key=None):
    if not key:
        raise MissingKey('Missing auth key')
    if not match(r'\w{32}:\w{40}', key):
        raise InvalidKey('Invalid key')
    return {'Authorization': f'Basic {str(b64encode(key.encode("UTF-8")), "UTF-8")}'}


def get_header():
    headers = {'User-Agent': f'Pyrecard - {VERSION}', 'Content-Type': 'application/json'}
    if environ.get('PYRECARD_ENV', '').lower() == 'production':
        return {**headers, **get_b64(environ.get('PRODUCTION_KEY'))}
    return {**headers, **get_b64(environ.get('SANDBOX_KEY'))}
