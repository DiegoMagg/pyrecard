from pyrecard.utils.pyrequest import pyrequest


CUSTOMER_URL = '/v2/customers'


def create(json):
    return pyrequest('POST', f'{CUSTOMER_URL}/', json)


def add_credit_card(customer_id, json):
    return pyrequest('POST', f'{CUSTOMER_URL}/{customer_id}/fundinginstruments', json)


def fetch(customer_id):
    return pyrequest('GET', f'{CUSTOMER_URL}/{customer_id}')


def fetch_all():
    return pyrequest('GET', CUSTOMER_URL)


def remove_credit_card(creditcard_id):
    return pyrequest('DELETE', f'/v2/fundinginstruments/{creditcard_id}')
