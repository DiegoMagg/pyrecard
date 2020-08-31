from pyrecard.utils.pyrequest import pyrequest


PLAN_PATH = '/assinaturas/v1/plans'


def create(json):
    return pyrequest('POST', PLAN_PATH, json)


def alter(plan_code, json):
    return pyrequest('PUT', f'{PLAN_PATH}/{plan_code}', json)


def activate(plan_code):
    return pyrequest('PUT', f'{PLAN_PATH}/{plan_code}/activate')


def inactivate(plan_code):
    return pyrequest('PUT', f'{PLAN_PATH}/{plan_code}/inactivate')


def fetch(plan_code):
    return pyrequest('GET', f'{PLAN_PATH}/{plan_code}')


def fetch_all():
    return pyrequest('GET', PLAN_PATH)
