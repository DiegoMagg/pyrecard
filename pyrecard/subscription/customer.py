from pyrecard.utils.pyrequest import pyrequest


CUSTOMER_PATH = '/assinaturas/v1/customers'


def create(json, new_vault=False):
    return pyrequest('POST', f'{CUSTOMER_PATH}?new_vault={new_vault}', json)


def alter(customer_code, json):
    return pyrequest('PUT', f'{CUSTOMER_PATH}/{customer_code}', json)


def fetch(customer_code):
    return pyrequest('GET', f'{CUSTOMER_PATH}/{customer_code}')


def fetch_all():
    return pyrequest('GET', CUSTOMER_PATH)


def change_card(customer_code, json):
    return pyrequest('PUT', f'{CUSTOMER_PATH}/{customer_code}/billing_infos', json)
