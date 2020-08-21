from os import environ
from requests.models import Response
from re import match
from base64 import b64encode
from pyrecard.exceptions import MissingKey, InvalidKey
from pyrecard.__version__ import __version__
from json import dumps


def url_factory(path=''):
    url = 'https://{}.moip.com.br/assinaturas/v1{}'
    production = environ.get('PYRECARD_ENV') == 'production'
    return url.format('api', path) if production else url.format('sandbox', path)


def response_factory(status_code, json):
    response = Response()
    response.status_code = status_code
    response._content = f'{dumps(json)}'.encode('UTF-8')
    return response


def b64_factory(key=None):
    if not key:
        raise MissingKey('Missing auth key')
    if not match(r'\w{32}:\w{40}', key):
        raise InvalidKey('Invalid key')
    return {'Authorization': f'Basic {str(b64encode(key.encode("UTF-8")), "UTF-8")}'}


def header_factory():
    headers = {'User-Agent': f'Pyrecard - {__version__}', 'Content-Type': 'application/json'}
    if environ.get('PYRECARD_ENV', '').lower() == 'production':
        return {**headers, **b64_factory(environ.get('PRODUCTION_KEY'))}
    return {**headers, **b64_factory(environ.get('SANDBOX_KEY'))}
