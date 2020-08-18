from os import environ
from base64 import b64encode
from exceptions import MissingKey


def get_auth_header():
    headers = {'Authorization': None, 'Content-Type': 'application/json'}
    key = environ.get('WIRECARD_KEY')
    if key:
        headers['Authorization'] = 'Basic ' + str(b64encode(key.encode('utf-8')), 'UTF-8')
        return headers
    raise MissingKey('Wirecard key not found.')
