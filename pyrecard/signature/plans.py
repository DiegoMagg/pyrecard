import requests
from common.auth import get_auth_header
from common.urls import get_url


def create(json):
    return requests.post(get_url('/plans'), headers=get_auth_header(), json=json)


def alter(code, json):
    return requests.put(get_url(f'/plans/{code}'), headers=get_auth_header(), json=json)


def fetch(code):
    return requests.get(get_url(f'/plans/{code}'), headers=get_auth_header())


def fetch_all():
    return requests.get(get_url('/plans'), headers=get_auth_header())
