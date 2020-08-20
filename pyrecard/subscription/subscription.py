import requests
from os import environ
from pyrecard.utils.factory import url_factory, response_factory, header_factory
from pyrecard.decorators import set_response_timeout


@set_response_timeout
def create(json, new_customer=False):
    return requests.post(
        url_factory(f'/subscriptions?new_customer={new_customer}'),
        headers=header_factory(),
        json=json,
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def fetch(code):
    return requests.get(
        url_factory(f'/subscriptions/{code}'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def fetch_all():
    return requests.get(
        url_factory('/subscriptions'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def set_status(code, status):
    message = 'The subscription status must be "suspend", "activate" or "cancel"'
    if str(status).lower() not in ['suspend', 'activate', 'cancel']:
        return response_factory(400, {'error': message})
    return requests.put(
        url_factory(f'/subscriptions/{code}/{status}'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def alter(code, json):
    return requests.put(
        url_factory(f'/subscriptions/{code}'),
        headers=header_factory(), json=json,
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def set_payment_method(code, method):
    if str(method).upper() not in ['CREDIT_CARD', 'BOLETO']:
        return response_factory(400, {'error': 'The payment method must be "CREDIT_CARD" or "BOLETO"'})
    return requests.put(
        url_factory(f'/subscriptions/{code}/change_payment_method'),
        headers=header_factory(),
        json={'payment_method': method.upper()},
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def fetch_all_invoices(code):
    return requests.get(
        url_factory(f'/subscriptions/{code}/invoices'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )
