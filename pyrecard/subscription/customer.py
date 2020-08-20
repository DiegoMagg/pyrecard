import requests
from os import environ
from pyrecard.utils.factory import header_factory, url_factory
from pyrecard.decorators import set_response_timeout


@set_response_timeout
def create(json, new_vault=False):
    return requests.post(
        url_factory(f'/customers?new_vault={new_vault}'),
        headers=header_factory(),
        json=json,
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def alter(code, json):
    return requests.put(
        url_factory(f'/customers/{code}'),
        headers=header_factory(),
        json=json,
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def fetch(code):
    return requests.get(
        url_factory(f'/customers/{code}'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def fetch_all():
    return requests.get(
        url_factory('/customers'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def change_card(code, json):
    return requests.put(
        url_factory(f'/customers/{code}/billing_infos'),
        headers=header_factory(),
        json=json,
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )
