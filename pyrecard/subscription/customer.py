from pyrecard.utils.pyrequest import pyrequest


def create(json, new_vault=False):
    return pyrequest('POST', f'/customers?new_vault={new_vault}', json)


def alter(customer_code, json):
    return pyrequest('PUT', f'/customers/{customer_code}', json)


def fetch(customer_code):
    return pyrequest('GET', f'/customers/{customer_code}')


def fetch_all():
    return pyrequest('GET', '/customers')


def change_card(customer_code, json):
    return pyrequest('PUT', f'/customers/{customer_code}/billing_infos', json)
