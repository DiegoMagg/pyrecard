import requests
from pyrecard.common.auth import get_header
from pyrecard.common.urls import get_url


def fetch_invoice(code):
    return requests.get(get_url(f'/invoices/{code}'), headers=get_header())


def fetch_invoice_payments(code):
    return requests.get(get_url(f'/invoices/{code}/payments'), headers=get_header())


def payment_details(code):
    return requests.get(get_url(f'/payments/{code}'), headers=get_header())
