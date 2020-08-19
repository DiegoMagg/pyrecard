import requests
from pyrecard.common.auth import get_header
from pyrecard.common.urls import get_url


def create(json, new_customer=False):
    return requests.post(
        get_url(f'/subscriptions?new_customer={new_customer}'), headers=get_header(), json=json,
    )


def fetch(code):
    return requests.get(get_url(f'/subscriptions/{code}'), headers=get_header())


def fetch_all():
    return requests.get(get_url('/subscriptions'), headers=get_header())


def set_status(code, status):
    return requests.put(get_url(f'/subscriptions/{code}/{status}'), headers=get_header())


def change(code, json):
    return requests.put(get_url(f'/subscriptions/{code}'), headers=get_header(), json=json)


def set_payment_method(code, method):
    if method.upper() not in ['CREDIT_CARD', 'BOLETO']:
        raise ValueError('The payment method must be "CREDIT_CARD" or "BOLETO"')
    return requests.put(
        get_url(f'/subscriptions/{code}/change_payment_method'),
        headers=get_header(),
        json={"payment_method": method.upper()},
    )


def get_all_invoices(subscription_code):
    return requests.get(get_url(f'/subscriptions/{subscription_code}/invoices'), headers=get_header())
