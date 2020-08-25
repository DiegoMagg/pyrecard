from pyrecard.utils.pyrequest import pyrequest
from pyrecard.subscription.subscription import alter
from pyrecard.utils.factory import response_factory


COUPON_PATH = '/assinaturas/v1/coupons'


def create(json):
    return pyrequest('POST', COUPON_PATH, json)


def apply(subscription_code, coupon_code):
    return alter(subscription_code, {'coupon': {'code': coupon_code}})


def fetch(coupon_code):
    return pyrequest('GET', f'{COUPON_PATH}/{coupon_code}')


def fetch_all():
    return pyrequest('GET', COUPON_PATH)


def set_status(coupon_code, status):
    if str(status).lower() not in ('active', 'inactive'):
        return response_factory(400, {'error': 'The coupon status must be "active" or "inactive"'})
    return pyrequest('PUT', f'{COUPON_PATH}/{coupon_code}/{status}')


def remove(coupon_code):
    return pyrequest('DELETE', f'/assinaturas/v1/subscriptions/{coupon_code}/coupon')
