import requests
from pyrecard.common.auth import get_header
from pyrecard.common.urls import get_url


def create(json, new_vault=False):
    return requests.post(get_url(f'/customers?new_vault={new_vault}'), headers=get_header(), json=json)


def alter(code, json):
    return requests.put(get_url(f'/customers/{code}'), headers=get_header(), json=json)


def fetch(code):
    return requests.get(get_url(f'/customers/{code}'), headers=get_header())


def fetch_all():
    return requests.get(get_url('/customers'), headers=get_header())


def change_card(code, json):
    return requests.put(get_url(f'/customers/{code}/billing_infos'), headers=get_header(), json=json)
