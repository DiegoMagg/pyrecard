from pyrecard.utils.pyrequest import pyrequest


def create(json):
    return pyrequest('POST', '/plans', json)


def alter(plan_code, json):
    return pyrequest('PUT', f'/plans/{plan_code}', json)


def activate(plan_code):
    return pyrequest('PUT', f'/plans/{plan_code}/activate')


def inactivate(plan_code):
    return pyrequest('PUT', f'/plans/{plan_code}/inactivate')


def fetch(plan_code):
    return pyrequest('GET', f'/plans/{plan_code}')


def fetch_all():
    return pyrequest('GET', '/plans')
