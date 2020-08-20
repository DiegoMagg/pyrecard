import requests
from os import environ
from pyrecard.utils.factory import url_factory, header_factory
from pyrecard.decorators import set_response_timeout


@set_response_timeout
def create(json):
    return requests.post(
        url_factory('/plans'), headers=header_factory(),
        json=json,
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def alter(code, json):
    return requests.put(
        url_factory(f'/plans/{code}'), headers=header_factory(),
        json=json,
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def activate(code):
    return requests.put(
        url_factory(f'/plans/{code}/activate'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def inactivate(code):
    return requests.put(
        url_factory(f'/plans/{code}/inactivate'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def fetch(code):
    return requests.get(
        url_factory(f'/plans/{code}'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def fetch_all():
    return requests.get(
        url_factory('/plans'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )
