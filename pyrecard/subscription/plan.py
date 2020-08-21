from pyrecard.utils.pyrequest import pyrequest


def create(json):
    return pyrequest('POST', '/plans', json)


def alter(code, json):
    return pyrequest('PUT', f'/plans/{code}', json)


def activate(code):
    return pyrequest('PUT', f'/plans/{code}/activate')


def inactivate(code):
    return pyrequest('PUT', f'/plans/{code}/inactivate')


def fetch(code):
    return pyrequest('GET', f'/plans/{code}')


def fetch_all():
    return pyrequest('GET', '/plans')
