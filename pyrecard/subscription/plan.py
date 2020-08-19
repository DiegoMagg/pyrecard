import requests
from pyrecard.common.auth import get_header
from pyrecard.common.urls import get_url


def create(json):
    return requests.post(get_url('/plans'), headers=get_header(), json=json)


def alter(code, json):
    return requests.put(get_url(f'/plans/{code}'), headers=get_header(), json=json)


def activate(code):
    return requests.put(get_url(f'/plans/{code}/activate'), headers=get_header())


def inactivate(code):
    return requests.put(get_url(f'/plans/{code}/inactivate'), headers=get_header())


def fetch(code):
    return requests.get(get_url(f'/plans/{code}'), headers=get_header())


def fetch_all():
    return requests.get(get_url('/plans'), headers=get_header())
