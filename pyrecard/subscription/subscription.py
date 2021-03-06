from pyrecard.utils.pyrequest import pyrequest
from pyrecard.utils.factory import response_factory


SUBSCRIPTION_PATH = '/assinaturas/v1/subscriptions'


def create(json, new_customer=False):
    return pyrequest('POST', f'{SUBSCRIPTION_PATH}?new_customer={new_customer}', json)


def fetch(subscription_code):
    return pyrequest('GET', f'{SUBSCRIPTION_PATH}/{subscription_code}')


def fetch_all():
    return pyrequest('GET', SUBSCRIPTION_PATH)


def set_status(subscription_code, status):
    message = 'The subscription status must be "suspend", "activate" or "cancel"'
    if str(status).lower() not in ('suspend', 'activate', 'cancel'):
        return response_factory(400, {'error': message})
    return pyrequest('PUT', f'{SUBSCRIPTION_PATH}/{subscription_code}/{status}')


def alter(subscription_code, json):
    return pyrequest('PUT', f'{SUBSCRIPTION_PATH}/{subscription_code}', json)


def set_payment_method(subscription_code, method):
    if str(method).upper() not in ('CREDIT_CARD', 'BOLETO'):
        return response_factory(400, {'error': 'The payment method must be "CREDIT_CARD" or "BOLETO"'})
    return pyrequest(
        'PUT',
        f'{SUBSCRIPTION_PATH}/{subscription_code}/change_payment_method',
        json={'payment_method': method.upper()},
    )


def fetch_all_invoices(subscription_code):
    return pyrequest('GET', f'{SUBSCRIPTION_PATH}/{subscription_code}/invoices')
