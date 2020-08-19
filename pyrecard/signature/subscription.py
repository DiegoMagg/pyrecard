import requests
from common.auth import get_auth_header
from common.urls import get_url


def create(json, new_customer=False):
    return requests.post(
        get_url(f'/subscriptions?new_customer={new_customer}'), headers=get_auth_header(), json=json,
    )


def fetch(code):
    return requests.get(get_url(f'/subscriptions/{code}'), headers=get_auth_header())


def fetch_all():
    return requests.get(get_url('/subscriptions'), headers=get_auth_header())


def set_status(code, status):
    return requests.put(get_url(f'/subscriptions/{code}/{status}'), headers=get_auth_header())


def change(code, json):
    return requests.put(get_url(f'/subscriptions/{code}'), headers=get_auth_header(), json=json)


def set_payment_method(code, method):
    return requests.put(
        get_url(f'/subscriptions/{code}/change_payment_method'),
        headers=get_auth_header(),
        json={"payment_method": method.upper()},
    )
