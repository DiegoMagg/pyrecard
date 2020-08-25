from pyrecard.utils.pyrequest import pyrequest
from pyrecard.subscription.subscription import alter
from pyrecard.utils.factory import response_factory


def create(json):
    return pyrequest('POST', '/coupons', json)


def apply(subscription_code, coupon_code):
    return alter(subscription_code, {'coupon': {'code': coupon_code}})


def fetch(coupon_code):
    return pyrequest('GET', f'/coupons/{coupon_code}')


def fetch_all():
    return pyrequest('GET', '/coupons')


def set_status(coupon_code, status):
    if str(status).lower() not in ('active', 'inactive'):
        return response_factory(400, {'error': 'The coupon status must be "active" or "inactive"'})
    return pyrequest('PUT', f'/coupons/{coupon_code}/{status}')


def remove(coupon_code):
    return pyrequest('DELETE', f'/subscriptions/{coupon_code}/coupon')
