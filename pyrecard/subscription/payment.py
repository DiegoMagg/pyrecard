import requests
from os import environ
from pyrecard.utils.factory import url_factory, header_factory
from pyrecard.decorators import set_response_timeout


@set_response_timeout
def fetch_invoice(code):
    return requests.get(
        url_factory(f'/invoices/{code}'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def fetch_invoice_payments(code):
    return requests.get(
        url_factory(f'/invoices/{code}/payments'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )


@set_response_timeout
def payment_details(code):
    return requests.get(
        url_factory(f'/payments/{code}'),
        headers=header_factory(),
        timeout=float(environ.get('PYRECARD_REQUEST_TIMEOUT', 5)),
    )
