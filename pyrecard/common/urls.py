from os import environ


def get_url(path=''):
    url = 'https://{}.moip.com.br/assinaturas/v1{}'
    production = environ.get('PYRECARD_ENV') == 'production'
    return url.format('api', path) if production else url.format('sandbox', path)
