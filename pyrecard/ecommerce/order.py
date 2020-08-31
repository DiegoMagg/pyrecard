from pyrecard.utils.pyrequest import pyrequest

ORDER_URL = '/v2/orders'


def create(json):
    return pyrequest('POST', f'{ORDER_URL}/', json)


def fetch(code):
    return pyrequest('GET', f'{ORDER_URL}/{code}')


def fetch_all():
    return pyrequest('GET', ORDER_URL)
