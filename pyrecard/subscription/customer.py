from pyrecard.utils.pyrequest import pyrequest


def create(json, new_vault=False):
    return pyrequest('POST', f'/customers?new_vault={new_vault}', json)


def alter(code, json):
    return pyrequest('PUT', f'/customers/{code}', json)


def fetch(code):
    return pyrequest('GET', f'/customers/{code}')


def fetch_all():
    return pyrequest('GET', '/customers')


def change_card(code, json):
    return pyrequest('PUT', f'/customers/{code}/billing_infos', json)
