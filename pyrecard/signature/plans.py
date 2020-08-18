import requests
from common.auth import get_auth_header

URL = 'https://sandbox.moip.com.br/assinaturas/v1/plans'


def create(json):
    return requests.post(URL, headers=get_auth_header(), json=json)


def fetch(code):
    return requests.get(URL + f'/{code}', headers=get_auth_header())


def alter(code, json):
    return requests.put(URL + f'/{code}', headers=get_auth_header(), json=json)
