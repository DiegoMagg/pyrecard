from pyrecard.utils.pyrequest import pyrequest
from pyrecard.subscription.subscription import alter


def create(json):
    return pyrequest('POST', '/coupons', json)


def apply(code, json):
    return alter(code, json)


def fetch(code):
    return pyrequest('GET', f'/coupons/{code}')


def fetch_all():
    return pyrequest('GET', '/coupons')


def set_status(code, status):
    return pyrequest('PUT', f'/coupons/{code}/{status}')


def remove(code):
    return pyrequest('DELETE', f'/subscriptions/{code}/coupon')
